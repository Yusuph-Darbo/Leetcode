-- Approach:
-- Select customers whose referee is not 2 or who have no referee.
--
-- Time: O(n)
-- Space: O(1)

-- Write your PostgreSQL query statement below
select name from Customer
where referee_id != 2 or referee_id is null;