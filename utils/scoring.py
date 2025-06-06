def calculate_score(events, feedback_score):
    pr_count = sum(1 for e in events if e['type'] == 'PullRequestEvent')
    issue_count = sum(1 for e in events if e['type'] == 'IssuesEvent')

    return pr_count * 2 + issue_count + feedback_score * 5
