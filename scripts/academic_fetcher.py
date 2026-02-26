#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical AI Research Briefing Bot - Unified API-less Academic Fetcher
直接从 Europe PMC (免 API Key, 全源聚合) 拉取文献。
原生覆盖：PubMed, PMC, medRxiv, bioRxiv, arXiv, Nature 等所有医疗/AI核心期刊与预印本。
"""

import sys
import argparse
import urllib.request
import urllib.parse
import json
from urllib.error import URLError, HTTPError

TIMEOUT = 15
UA = "Mozilla/5.0 (compatible; MedicalAIBotFetcher/2.0; +https://github.com/nexusera/medical-ai-research-briefing-bot)"

def log(msg: str) -> None:
    """内部调试信息写入 stderr，不污染大模型读取的 stdout"""
    print(msg, file=sys.stderr)

def fetch_europe_pmc(query: str, max_results: int = 10, sort_by_date: bool = True) -> list[dict]:
    """从 Europe PMC REST API 拉取聚合文献 (涵盖 PubMed, arXiv, medRxiv)"""
    # Europe PMC 支持的排序：FIRST_PDATE_D desc (按日期降序)
    sort_query = " sort_date:y" if sort_by_date else ""
    # 对 query 进行 URL 编码
    safe_query = urllib.parse.quote(f"({query}){sort_query}")
    
    # 构建请求 URL (使用 cursorMark=* 获取第一页，resultType=core 获取摘要)
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={safe_query}&format=json&resultType=core&pageSize={max_results}&cursorMark=*"
    
    log(f"Fetching Europe PMC: {url}")
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except (URLError, HTTPError, OSError, json.JSONDecodeError) as e:
        log(f"Fetch or parse failed: {e}")
        return []

    results = data.get('resultList', {}).get('result', [])
    papers = []
    
    for item in results:
        # 提取来源/期刊名 (Nature, arXiv, medRxiv, etc.)
        journalTitle = item.get('journalTitle', item.get('pubType', 'Unknown Venue'))
        if item.get('bookOrReportDetails'):
            journalTitle = item['bookOrReportDetails'].get('publisher', journalTitle)
            
        # 提取链接 (优先选 DOI 链接，其次 Europe PMC 内部链接)
        url = f"https://europepmc.org/article/{item.get('source')}/{item.get('pmid') or item.get('id')}"
        if item.get('doi'):
            url = f"https://doi.org/{item.get('doi')}"
            
        # 作者列表提取
        authors = []
        author_list = item.get('authorList', {}).get('author', [])
        for a in author_list:
            if 'fullName' in a:
                authors.append(a['fullName'])
            elif 'lastName' in a:
                authors.append(f"{a.get('lastName', '')} {a.get('initials', '')}".strip())
        author_str = ", ".join(authors) if authors else "Unknown"

        # 时间提炼
        date = item.get('firstPublicationDate', item.get('pubYear', 'Unknown Date'))
        
        # 摘要提炼
        abstract = item.get('abstractText', 'No Abstract Available.')

        papers.append({
            "source": journalTitle,
            "title": item.get('title', 'No Title'),
            "authors": author_str,
            "date": date,
            "url": url,
            "abstract": abstract
        })
        
    return papers

def format_for_llm(papers: list[dict], search_query: str) -> str:
    """按人类可读和 LLM 易拆解的格式输出"""
    if not papers:
        return f"=== NO RESULTS FOUND FOR: [{search_query}] ==="
        
    output = []
    output.append(f"=== SEARCH RESULTS FOR: [{search_query}] ===")
    output.append(f"TOTAL FOUND: {len(papers)}\n")
    
    for idx, p in enumerate(papers, 1):
        output.append(f"--- PAPER {idx} ---")
        output.append(f"VENUE/SOURCE: {p['source']}")
        output.append(f"TITLE: {p['title']}")
        output.append(f"AUTHORS: {p['authors']}")
        output.append(f"PUBLISHED: {p['date']}")
        output.append(f"URL: {p['url']}")
        output.append(f"ABSTRACT:\n{p['abstract']}\n")
    
    output.append("=== END OF RESULTS ===")
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Fetch top medical & AI papers across ALL open databases via Europe PMC.")
    parser.add_argument("query", type=str, help="The Boolean search concept/query (e.g., 'OCR LLM pathology')")
    parser.add_argument("--max", type=int, default=10, help="Max total results to fetch")
    
    args = parser.parse_args()
    
    papers = fetch_europe_pmc(args.query, args.max)
    
    # 打印至 stdout
    print(format_for_llm(papers, args.query))

if __name__ == "__main__":
    main()
