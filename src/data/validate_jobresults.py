

def validate_results(results):
    valid_results = []
    for result in results:
        entry = {}
        if result['jobtitle']:
            entry['jobtitle'] = result['jobtitle']
        else:
            continue
        if result["url"]:
            entry['url'] = result['url']
        else:
            continue
        if result['jobkey']:
            entry['jobkey'] = result['jobkey']
        else:
            continue
        if result['company']:
            entry['company'] = result['company']
        else:
            continue
        if result['date']:
            # convert the date to datetime
            pass
        else:
            continue
        if result['city']:
            entry['city'] = result['city']
        else:
            continue
        if result['state']:
            entry['state'] = result['state']
        else:
            continue
        if result['formattedRelativeTime']:
            entry['relativeTime'] = result['formattedRelativeTime']
        else:
            continue
        valid_results.append(entry)
    return valid_results
