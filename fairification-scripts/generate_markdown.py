#!/usr/bin/env python3

import json
import argparse
from collections import Counter, defaultdict


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def status_value(check):
    return check.get("output", "unknown").strip().lower()


def indicator_name(check):
    indicator = check.get("assessesIndicator", {})
    return indicator.get("@id", "unknown").split("/")[-1]


def build_markdown(data):
    name = data.get("name", "Software Quality Assessment")
    description = data.get("description", "")
    date_created = data.get("dateCreated", "unknown")
    assessed = data.get("assessedSoftware", {})
    software_name = assessed.get("name", "unknown")
    software_url = assessed.get("url", "")
    checks = data.get("checks", [])

    counts = Counter(status_value(check) for check in checks)
    total = len(checks)

    by_indicator = defaultdict(list)
    for check in checks:
        by_indicator[indicator_name(check)].append(check)

    def escape_html(text):
        text = str(text)
        return (
            text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
        )

    def make_anchor(text):
        anchor = str(text).strip().lower()
        anchor = anchor.replace(" ", "-")
        anchor = anchor.replace("/", "-")
        anchor = anchor.replace(".", "")
        anchor = anchor.replace(":", "")
        return anchor

    def row_color(output):
        output = str(output).strip().lower()
        if output == "true":
            return "#d4edda"   # light green
        if output == "false":
            return "#f8d7da"   # light red
        return "#fff3cd"       # light yellow for error/unknown

    md = []

    md.append(f"# {name}\n")
    if description:
        md.append(f"{description}\n")

    md.append("## General Information\n")
    md.append(f"- **Software:** {software_name}")
    if software_url:
        md.append(f"- **Repository:** {software_url}")
    md.append(f"- **Assessment date:** {date_created}")
    md.append(f"- **Total checks:** {total}\n")

    md.append("## Summary\n")
    md.append(f"- **Passed (`true`)**: {counts.get('true', 0)}")
    md.append(f"- **Failed (`false`)**: {counts.get('false', 0)}")
    md.append(f"- **Errors (`error`)**: {counts.get('error', 0)}\n")

    md.append("## Results Table\n")
    md.append('<table>')
    md.append('  <thead>')
    md.append('    <tr>')
    md.append('      <th>Test ID</th>')
    md.append('      <th>Test Name</th>')
    md.append('      <th>Result</th>')
    md.append('    </tr>')
    md.append('  </thead>')
    md.append('  <tbody>')

    for check in checks:
        test_id = escape_html(check.get("test_id", ""))
        test_name = escape_html(check.get("test_name", ""))
        output = status_value(check)
        output_html = escape_html(output)

        ind = indicator_name(check)
        detail_anchor = make_anchor(f"{ind}-{check.get('test_id', '')}")

        md.append(f'    <tr style="background-color: {row_color(output)};">')
        md.append(f'      <td>{test_id}</td>')
        md.append(f'      <td>{test_name}</td>')
        md.append(f'      <td><a href="#{detail_anchor}">{output_html}</a></td>')
        md.append('    </tr>')

    md.append('  </tbody>')
    md.append('</table>\n')

    md.append("## Detailed Results by Indicator\n")

    for ind in sorted(by_indicator):
        md.append(f"### {ind}\n")
        for check in by_indicator[ind]:
            detail_anchor = make_anchor(f"{ind}-{check.get('test_id', '')}")
            md.append(f'<a id="{detail_anchor}"></a>')
            md.append(f"#### {check.get('test_name', 'Unnamed test')}\n")
            md.append(f"- **Test ID:** {check.get('test_id', '')}")
            md.append(f"- **Result:** {status_value(check)}")
            md.append(f"- **Process:** {check.get('process', 'N/A')}")
            md.append(f"- **Evidence:** {check.get('evidence', 'N/A')}")
            md.append(f"- **Suggestions:** {check.get('suggestions', 'N/A')}\n")

    return "\n".join(md)


def save_markdown(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(
        description="Convert RSFC JSON assessment report to Markdown."
    )
    parser.add_argument("input", help="Input JSON report file")
    parser.add_argument("output", help="Output Markdown file")

    args = parser.parse_args()

    data = load_json(args.input)
    markdown = build_markdown(data)
    save_markdown(args.output, markdown)

    print(f"Markdown report generated: {args.output}")


if __name__ == "__main__":
    main()