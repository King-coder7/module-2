# Overview

As a software engineer, I am focused on mastering cloud-native architectures and real-time data synchronization. My goal with this project was to move beyond local file storage and build a scalable system that leverages industry-standard NoSQL databases to handle persistence and data isolation effectively.

This software is a **Cloud Task Manager** built in Python that integrates directly with **Google Firebase Firestore**. It allows users to create, view, update, and delete tasks in real-time. The program uses a command-line interface (CLI) to interact with the database, featuring a custom "Seed" script to populate data and specialized queries to filter tasks by status. To use the program, ensure your credentials are in place and run `python3 app.py` to navigate the interactive menu.

The purpose of writing this software was to gain hands-on experience with asynchronous cloud communication and to implement a professional-grade schema that handles data isolation, ensuring users only interact with their own specific datasets.

[Software Demo Video](https://youtu.be/hcFqYIB4pTQ)

# Cloud Database

I am using **Google Firebase Firestore**, a flexible, scalable NoSQL document database. I chose Firestore for its real-time capabilities and seamless integration with Python via the `firebase-admin` SDK.

The database is structured into a single collection named `tasks`. Each document in this collection represents a unique task and contains the following fields:
* **user_id**: A string used for data isolation to identify task ownership.
* **title**: A string containing the task description.
* **status**: A string indicating if the task is "Pending" or "Completed".
* **created_at**: A server-generated timestamp for chronological sorting.



# Development Environment

To develop this software, I used **Visual Studio Code** on macOS. For version control, I used **Git** and **GitHub**, following a strict routine to synchronize progress across multiple physical locations and protect sensitive service account credentials using `.gitignore`.

The project is written in **Python 3.9+**. Key libraries include:
* **firebase-admin**: Used for authenticating and communicating with the Google Cloud Firestore API.
* **datetime**: Used for generating local timestamps for task tracking.

# Useful Websites

- [Firebase Python SDK Documentation](https://firebase.google.com/docs/firestore/quickstart)
- [GitHub Secret Scanning & Push Protection](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)
- [Python Firebase Admin Setup Guide](https://firebase.google.com/docs/admin/setup)

# Future Work

- **User Authentication**: Replace hardcoded UIDs with Firebase Auth for secure, real-time login.
- **Enhanced Sorting**: Implement complex queries to sort tasks by priority levels or due dates.
- **Batch Operations**: Add the ability to mark multiple tasks as "Completed" in a single database transaction.