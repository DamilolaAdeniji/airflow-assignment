SELECT page_title, SUM(count_views) total_views
FROM pageviews_data
GROUP BY page_title
ORDER BY SUM(count_views) DESC
LIMIT 1