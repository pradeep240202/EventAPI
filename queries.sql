-- Write a custom SQL query to fetch the total tickets sold for all events along with event details.
--  The query should optimize for large datasets and return the top 3 events by tickets sold.

SELECT e.id, e.name, e.date, e.total_tickets, e.tickets_sold
FROM events_event e
ORDER BY e.tickets_sold DESC
LIMIT 3;