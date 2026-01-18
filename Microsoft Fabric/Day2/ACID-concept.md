# Database ACID Properties (with Simple Transaction Example)

ACID properties ensure that database transactions are **reliable, consistent, and safe**, even during failures or concurrent access.

---

## Example Transaction: Bank Transfer

**Scenario:** Transfer **₹1,000** from **Account A** to **Account B**

**Steps:**
1. Debit ₹1,000 from Account A  
2. Credit ₹1,000 to Account B  

---

## <span style="color:#1f77b4"><strong>Atomicity</strong></span> — All or Nothing

**Definition:**  
A transaction must either **complete fully** or **not happen at all**.

**Example:**  
- ₹1,000 is debited from Account A  
- System crashes before crediting Account B  

**What happens:**  
- The debit is **rolled back**  
- Account A gets its ₹1,000 back  

**Key Point:**  
No partial transaction is allowed.

---

## <span style="color:#2ca02c"><strong>Consistency</strong></span> — Rules Are Preserved

**Definition:**  
A transaction must move the database from **one valid state to another valid state**.

**Example Rules:**  
- Account balance cannot be negative  
- Total money before and after transfer must remain the same  

**What happens:**  
- If Account A has only ₹500, the transaction is **rejected**  
- All constraints and validations are enforced  

**Key Point:**  
Database data always remains **correct and valid**.

---

## <span style="color:#ff7f0e"><strong>Isolation</strong></span> — No Interference

**Definition:**  
Concurrent transactions should not affect each other.

**Example:**  
- Transaction T1 transfers ₹1,000  
- Transaction T2 reads Account A balance at the same time  

**What happens:**  
- T2 sees either:
  - Balance before the transfer, or  
  - Balance after the transfer  
- It never sees half-updated data  

**Key Point:**  
Transactions behave as if executed **one by one**.

---

## <span style="color:#d62728"><strong>Durability</strong></span> — Permanent Once Committed

**Definition:**  
Once a transaction is committed, its changes are **permanent**.

**Example:**  
- Transfer completes successfully  
- System crashes immediately afterward  

**What happens:**  
- After restart, the transfer is still present  
- Data is recovered from disk or logs  

**Key Point:**  
Committed data is **never lost**.

---


