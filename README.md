    
# 🚀 Odoo Internship Tasks

This repository contains a curated set of tasks and learning paths for interns focusing on Odoo development using RPC and API techniques. The tasks are structured for deeper learning, advanced implementation, and professional experience.

---

## ✅ Task List with User Stories

### 1. Expose Customer List via JSON-RPC
**User Story:**  
_As a developer, I want to expose customer data via a secure JSON-RPC endpoint, so that external systems can fetch customer info safely._

**Gherkin Acceptance Criteria:**
```gherkin
Scenario: Fetch customers with a valid token
  Given the API token is set
  When I send a JSON-RPC POST to /api/customers with the token
  Then I get a list of customer data
```

---

### 2. Mark as VIP via JS RPC
**User Story:**  
_As a developer, I want to mark customers as VIP using a JS RPC button, so that users can instantly update the record from UI._

**Gherkin Acceptance Criteria:**
```gherkin
Scenario: User clicks 'Mark as VIP'
  Given I am on the partner form
  When I click the VIP button
  Then the partner is updated and notification appears
```

---

### 3. Create CRM Lead via Public API
**User Story:**  
_As a developer, I want to allow external systems to create CRM leads with token auth, so that we can receive leads from 3rd parties._

**Gherkin Acceptance Criteria:**
```gherkin
Scenario: Create lead with valid token and data
  When I POST to /api/create_lead
  Then a lead is created and ID is returned
```

---

### 4. Sync Users from External API
**User Story:**  
_As a developer, I want to sync external users into Odoo, so that I can import 3rd party data into custom models._

**Gherkin Acceptance Criteria:**
```gherkin
Scenario: Trigger sync from button
  When I click "Sync Users"
  Then data from external API is imported
```

---

### 5. Get Today’s Attendance via JSON-RPC
**User Story:**  
_As a developer, I want to retrieve today's check-in/out data via JSON-RPC, so that the mobile app can show attendance info._

**Gherkin Acceptance Criteria:**
```gherkin
Scenario: Logged-in employee fetches attendance
  When I call /api/today_attendance
  Then I get check-in and check-out if present
```

---

## 📘 Deep Dive Topics for Advanced Learning

### 🔐 Secure Token Auth
- Use JWT or OAuth2
- Rotate & revoke keys
- Rate limit access

### 🔄 Sync & Integration
- Two-way data sync
- Conflict resolution
- Use RabbitMQ or Webhooks

### 🧠 OWL & JS Mastery
- Build custom widgets
- Use useState, useEffect
- Dynamic UI with RPC

### 🧪 Testing & CI/CD
- Unit tests with `odoo.tests.common`
- GitHub Actions with pylint, pytest
- Docker Compose for local dev

### 📊 Performance & Logging
- Optimize SQL queries
- Use `read_group`, `prefetch`
- Monitor with Prometheus

---

## 📁 Repository Layout (suggested)

```
/custom_addons/
  /api_security/
  /external_sync_base/
  /crm_lead_api/
  /attendance_mobile_api/
.gitignore
README.md
```

---

## 🛠 Getting Started

```bash
git clone https://github.com/your-org/odoo-internship-tasks.git
cd odoo-internship-tasks
# Install custom_addons in your Odoo
```

Happy coding and keep exploring! 💡
