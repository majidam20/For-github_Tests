## Introduction

We are a cross-functional team of data scientists, data engineers and software developers from multiple nationalities and with diverse backgrounds. Our mission is to support data-driven decision making in trivago's marketplace by providing end-to-end analytic tools, metrics & analyses.

A day in this job is dynamic, challenging, and never the same. We are looking for one more team mate to design and maintain the data pipelines that will enable the resulting structured data to be as useful as possible to the analytics teams at trivago.

This assignment is designed to assess your SQL skills and how you structure your thoughts. In addition to the correctness of the solution we will be looking at how you justify your choices. We are thrilled to get to know you a bit more through the way you solve the tasks.

For each of the tasks below we would like you to prepare an SQL query. Follow the instructions in the `README.md` file for details on how to prepare, test, and submit your solutions.

The compressed file that you received also contains expected outputs for the given example inputs. If any of the expected outputs does not make sense to you, then you can also modify them. However, in this case we expect you to thoroughly justify these changes.

## Task 1: calculate booking conversion

Given a set of hotels, as well as the clicks and bookings received by each of these hotels in a certain period of time, calculate the booking conversion rate (i.e. the fraction of clicks that get converted into bookings) per country, ordered by country name.

## Task 2: who traveled with their parents?

Given a list of travelers and a guest list of hotels the travelers stayed at, identify the set of travelers that may have stayed in the same hotel as one of their parents (ordered by name). Assume that there must be an age difference of at least 16 years between a child and their parents. 


## Task 3: help the hotel manager

You are asked to support the management of a hotel, more specifically **how many rooms** should be prepared and opened for each given week. We want to minimize the number of served rooms so that we also minimize maintenance costs. Assume that the number of guests is always 2 per room and that a room can always be made available the same day as the check-out date.

As input you are given a list of the reservations with the check-in and check-out dates.
