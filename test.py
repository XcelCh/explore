from explore import Explore
import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of rows
N = 5000

# ---------------------------------------------------------
# 1. Generate the dataset
# ---------------------------------------------------------

first_names = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ivan", "Julia"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Wilson", "Taylor"
]

departments = [
    "Engineering",
    "Marketing",
    "Finance",
    "Human Resources",
    "Sales",
    "Operations",
    "IT",
    "Research"
]

# Longer strings containing spaces, punctuation, numbers, and symbols
long_texts = [
    "Customer requested a refund!!! Ticket #A-1024 @ 10:30 AM.",
    "System check completed successfully -> status: OK [100%].",
    "Important: update password before 2026-12-31! #Security",
    "Order #ORD-5521 contains 3 items; total = $149.99.",
    "User feedback: 'Excellent service!' Rating = 5/5 ★",
    "Error detected: code=ERR_404; path=/api/v2/users?id=123.",
    "Meeting scheduled @ 14:30 -- Room #B-204 (online backup).",
    "Special characters: ! @ # $ % ^ & * ( ) _ + = - / \\ | < > ?",
    "Data imported from source [CRM-01] on 2026-08-24.",
    "Note: this is a longer text field with symbols, numbers (12345), "
    "punctuation, and mixed content! $$$"
]

# ---------------------------------------------------------
# 2. Create columns
# ---------------------------------------------------------

df = pd.DataFrame({
    # String / object column
    "name": [
        f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
        for _ in range(N)
    ],

    # Integer column
    "age": np.random.randint(18, 70, size=N),

    # Float column
    "salary": np.round(
        np.random.uniform(25000.00, 150000.00, size=N),
        2
    ),

    # Boolean column
    "is_active": np.random.choice(
        [True, False],
        size=N
    ),

    # Datetime column
    "join_date": pd.to_datetime(
        np.random.randint(
            pd.Timestamp("2020-01-01").value // 10**9,
            pd.Timestamp("2026-08-24").value // 10**9,
            size=N
        ),
        unit="s"
    ),

    # Category column
    "department": pd.Categorical(
        np.random.choice(
            departments,
            size=N
        ),
        categories=departments
    ),

    # Longer string/object column containing symbols
    "description": np.random.choice(
        long_texts,
        size=N
    ),

    # Integer column containing negative, zero, and positive values
    "balance_change": np.random.randint(
        -10000,
        10001,
        size=N
    )
})

# ---------------------------------------------------------
# 3. Explicitly set the requested data types
# ---------------------------------------------------------

df["name"] = df["name"].astype("object")
df["age"] = df["age"].astype("int64")
df["salary"] = df["salary"].astype("float64")
df["is_active"] = df["is_active"].astype("bool")
df["join_date"] = pd.to_datetime(df["join_date"])
df["department"] = df["department"].astype("category")
df["description"] = df["description"].astype("object")
df["balance_change"] = df["balance_change"].astype("int64")

exp = Explore(df)

print(exp.dtypes)

print('Numeric Summary:')
print(exp.numeric_summary())
print('\n')

print('Text Summary:')
print(exp.text_summary())
print('\n')

print('Category Summary:')
print(exp.category_summary())
print('\n')

print('Date Summary:')
print(exp.date_summary())
print('\n')

print('Boolean Summary:')
print(exp.bool_summary())
print('\n')