## 511
Select player_id, min(event_date) As first_login
From Activity
Group by player_id
;

## 512
# method 1
Select a.play_id, a.device_id
From Activity as a
Inner Join
(
Select play_id, min(event_date) As first_login
From Activity
Group by player_id
) b
On a.player_id = b.player_id And a.event_date = b.first_login
;

# method 2
Select player_id, device_id
From (
Select *, Rank() Over (Partition by player_id Order by event_date asc) as rank
From Activity
) tmp
Where rank = 1
;

## 534
Select player_id, event_date, 
sum(games_played) Over (Partition by player_id Order by event_date asc) AS games_played_so_far
From Activity
;

## 550
Select Round(sum(Case when b.event_date is not Null and tmp.first_login is not Null Then 1 Else 0 End) / count(Distinct a.player_id), 2) as fraction
From Activity a 
Left Join Activity b
On a.player_id = b.player_id and a.event_date = b.event_date - 1
Left Join 
(
	Select player_id, min(event_date) As first_login
	From Activity
	Group by player_id
) tmp
On a.player_id = b.player_id and a.event_date = tmp.first_login

## 570
Select b.Name
From Employee a
Left Join Employee b
On a.ManagerId = b.Id
Group by a.ManagerId
Having count(*) >= 5
;

## 571
With temp AS (
Select *, sum(Frequency) Over (Order by Number ASC) AS cum_freq
From Numbers
)

Select Avg(cum_freq)
From
(
Select 
Top (
Case when max(cum_freq)/2 = int(max(cum_freq)/2) and cum_freq-max(cum_freq)/2 > 1 Then 1 
	when max(cum_freq)/2 = int(max(cum_freq)/2) and cum_freq-max(cum_freq)/2 = 1 Then 2 
	When max(cum_freq)/2 <> int(max(cum_freq)/2) and cum_freq-max(cum_freq)/2 = 1 Then 1 
End) cum_freq 
From Numbers
Where cum_freq >= max(cum_freq)/2
Order by cum_freq asc
) tmp
;

# ref: https://zqt0.gitbook.io/leetcode/sql/571.hard-gei-ding-shu-zi-de-pin-lv-cha-xun-zhong-wei-shu
# directly by definition？ Don't know why
SELECT AVG(a.number) median
FROM Numbers a
WHERE a.frequency >= ABS(
    (SELECT SUM(frequency) FROM Numbers WHERE a.number <= number) - 
    (SELECT SUM(frequency) FROM Numbers WHERE a.number >= number))

## 574
Select Name
From (
	Select Name, rank() Over (Order by cnt desc) as rank
	From
		(
		Select Name, count(*) as cnt
		From Candidate c
		Inner Join Vote v
		On c.id = v.CandiateId
		Group by Name
		) tmp
) tmp2
Where rank = 1

## 577
Select name, bonus
From Employee e
Left Join Bonus b
On e.empId = b.empIb
Where bonus < 1000 or bonus is Null
;

## 578 
# assume no tie
Select question_id
From survey_log
Group by question_id
Order by count(answer_id) / sum(Case when action = 'show' Then 1 else 0 End) desc
Limit 1
;

## 579
Select a.id, a.month, sum(a.Salary) as Salary
From Employee a
Left Join Employee b
On a.Id = b.Id and a.month >= b.month and a.month <= b.month+2
Left join 
(
	Select Id, max(month)
	From Employee
	Group by Id
	) tmp
On a.Id = tmp.Id and a.Month = tmp.Month
Where tmp.month is Null
Group by a.id, a.month
Order by a.id, a.month desc
;

## 580
Select dept_name, sum(case when student_id is Null then 0 else 1 End) as student_number
From department d
Left Join student s
On d.dept_id = s.dept_id
;


## 584
# MySQL uses three-valued logic -- TRUE, FALSE and UNKNOWN. Anything compared to NULL evaluates to the third value
Select name
From customer
Where referee_id <> 2 or referee_id is NULL 
;

## 585
Select sum(tiv_2016)
From insurance as i
Inner Join
(
Select tiv_2015
From insurance
Group by tiv_2015
Having count(pid) > 1
) t1 
On i.tiv_2015 = t1.tiv_2015

Inner Join
(
Select lat, lon
From insurance
Group by lat, lon
Having count(pid) = 1
) t2 
On i.lat = t2.lat and i.lon = t2.lon

## 586
Select customer_number
From orders
Group by customer_number
Order by count(order_numer) desc
Limit 1
;
## 597
Select round(count(accepter_id) / count(send_to_id), 2) As accept_rate
From (
Select distinct sender_id, send_to_id, request_id, accepter_id
From friend_quest as a
Left Join request_accepted as b
On a.sender_id = b.requester_id and a.send_to_id = b.accepter_id
) tmp


