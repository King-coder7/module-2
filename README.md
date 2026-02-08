# Cloud Task Manager (Firestore)
**Developer:** Patrick Sano  
**Project:** CSE 310 Module 2 - Cloud Databases

## Overview
This is a Python-based Command Line Interface (CLI) application that manages tasks in a real-time Google Firebase Firestore database. It demonstrates full **CRUD** (Create, Read, Update, Delete) capabilities with a focus on data isolation and clean software engineering.

## Data Schema
To ensure a predictable structure, every document in the `tasks` collection follows this schema:

| Field | Type | Description |
| :--- | :--- | :--- |
| `user_id` | String | Unique identifier for data isolation (users only see their own tasks). |
| `title` | String | The description of the task. |
| `status` | String | Current state (e.g., "Pending" or "Completed"). |
| `created_at` | Timestamp | Server-generated time of creation for sorting. |



## Setup & Authentication
[cite_start]To mitigate configuration risks across different environments (Lab, Library, Home), this project uses **relative pathing**.

1. **Install Dependencies**: 
   ```bash
   python3 -m pip install firebase-admin