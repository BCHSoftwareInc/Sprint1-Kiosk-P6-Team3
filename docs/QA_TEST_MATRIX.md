# QA Test Execution Matrix - Sprint 1
* **QA Tester:** @kamal836
* **Client Deliverable:** Console Interactive Kiosk

| Test ID | Target Input Field | Test Input Description | Expected Output | Actual Behavior | Status (Pass/Fail) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Full Name | Standard text (`"Jane Doe"`) | Formatted correctly in ASCII box |  |  |
| TC-02 | Department/Role | Standard text (`"BCH Cybersecurity Division"`) | Correctly formatted |  |  |
| TC-03 | Email / Contact | Valid string (`"test@bch.org"`) | Stored & printed accurately |  |  |
| TC-04 | Badge Tier | Lowercase text (`"vip"`) | Clean output on badge |  |  |
| TC-05 | Full Name | Blank input (`""`) | Doesn't crash |  |  |
| TC-06 | Department/Role | Blank input (`""`) | Doesn't crash |  |  |
| TC-07 | Email / Contact | Blank input (`""`) | Doesn't crash |  |  |
| TC-08 | Badge Tier | Blank input (`""`) | Doesn't crash |  |  |
| TC-09 | Full Name | Boundary input (`"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"`) | Doesn't crash |  |  |
| TC-10 | Department/Role | Boundary input (`"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"`) | Doesn't crash |  |  |
| TC-11 | Email / Contact | Boundary input (`"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"`) | Doesn't crash |  |  |
| TC-12 | Badge Tier | Boundary input (`"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"`) | Doesn't crash |  |  |
