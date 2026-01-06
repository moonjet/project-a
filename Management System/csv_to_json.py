#!/usr/bin/env python3
"""
CSV to JSON Converter for AI Tools Directory
Usage: python csv_to_json.py
Converts ai-tools-data.csv to ai-tools-directory.json
"""

import csv
import json

def parse_list(text):
    """Convert pipe-separated string to list"""
    if not text or text.strip() == '':
        return []
    return [item.strip() for item in text.split('|')]

def parse_badges(text):
    """Convert comma-separated badges to list"""
    if not text or text.strip() == '':
        return []
    return [badge.strip() for badge in text.split(',')]

def build_pricing_tier(name, price, features_text):
    """Build a pricing tier object"""
    if not name or not price:
        return None

    features = parse_list(features_text)
    return {
        "name": name,
        "price": price,
        "features": features
    }

def build_timeline(dates_text, versions_text, events_text):
    """Build timeline array from pipe-separated strings"""
    if not dates_text or not versions_text or not events_text:
        return []

    dates = parse_list(dates_text)
    versions = parse_list(versions_text)
    events = parse_list(events_text)

    timeline = []
    for date, version, event in zip(dates, versions, events):
        timeline.append({
            "date": date,
            "version": version,
            "event": event
        })

    return timeline

def csv_to_json(csv_file='ai-tools-data.csv', json_file='ai-tools-directory.json'):
    """Convert CSV to JSON format"""

    # Group tools by category
    categories = {}

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            category_name = row['category']

            # Initialize category if new
            if category_name not in categories:
                categories[category_name] = {
                    "name": category_name,
                    "description": "",  # Add manually later if needed
                    "colorScheme": "primary",  # Default
                    "tools": []
                }

            # Build pricing tiers
            pricing_tiers = []
            for i in range(1, 4):  # Support up to 3 tiers
                tier = build_pricing_tier(
                    row.get(f'tier{i}_name', ''),
                    row.get(f'tier{i}_price', ''),
                    row.get(f'tier{i}_features', '')
                )
                if tier:
                    pricing_tiers.append(tier)

            # Build timeline
            timeline = build_timeline(
                row.get('timeline_dates', ''),
                row.get('timeline_versions', ''),
                row.get('timeline_events', '')
            )

            # Build tool object
            tool = {
                "name": row['name'],
                "url": row['url'],
                "description": row['description'],
                "badges": parse_badges(row['badges']),
                "rating": float(row['rating']) if row['rating'] else 0.0,
                "thumbnail": f"https://www.google.com/s2/favicons?domain={row['url'].replace('https://', '').replace('http://', '').split('/')[0]}&sz=128",
                "cornerBadge": row['cornerBadge'] if row['cornerBadge'] else None,
                "allBadges": parse_badges(row['allBadges']) if row['allBadges'] else [],
                "pricing": row['pricing'] if row['pricing'] else None,
                "pricingTiers": pricing_tiers if pricing_tiers else None,
                "timeline": timeline if timeline else None
            }

            categories[category_name]['tools'].append(tool)

    # Build final JSON structure
    output = {
        "categories": list(categories.values())
    }

    # Write to JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Converted {len(categories)} categories")
    total_tools = sum(len(cat['tools']) for cat in categories.values())
    print(f"✅ Total tools: {total_tools}")
    print(f"✅ Output: {json_file}")

if __name__ == '__main__':
    try:
        csv_to_json()
    except FileNotFoundError:
        print("❌ Error: ai-tools-data.csv not found!")
        print("   Make sure your CSV file is named 'ai-tools-data.csv'")
    except Exception as e:
        print(f"❌ Error: {e}")
