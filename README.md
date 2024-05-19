# Marchup-Test

## Overview

Marchup is a professional social network focused on students, providing a platform to connect, share opportunities, and grow professionally. This repository contains the source code for the Marchup test automation focused on Web, REST API, and Mobile App.

## Features

- **Student Profiles:** Create and manage profiles showcasing skills and experiences.
- **Job Posting:** Post and apply for jobs tailored for students.
- **Marchup Spaces:** Create spaces for initiatives such as non-profits, clubs, events.
- **Networking:** Connect with other students and professionals.
- **AI Tools:** Utilize AI for resume generation and more.

## Installation

Clone the repository along with its submodules:

```bash
git clone --recursive https://github.com/marchup-net/marchup-test
cd marchup-test
```

## Directory Structure

- **DEV_PROCESS.md:** Contains the development process documentation.
- **tests:** Contains all test-related files and directories.
  - **functional:** Contains functional tests.
  - **performance:** Contains performance tests.

## Running Tests

### Functional Tests

To run the functional tests:

```bash
cd tests/functional/web
pytest
```
