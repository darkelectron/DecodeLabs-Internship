# DecodeLabs Internship

Three Python CLI projects built during the DecodeLabs internship program for Python Programming.

_(period May 28 - June 28)_

## Projects

### Project 1: Todo List (`project_1/`)
A CLI todo list manager with SQLite persistence.
- Add, view, and manage tasks
- Auto-creates `todolist.db` on first run

```bash
python project_1/todolist.py
```

### Project 2: Expense Tracker (`project_2/`)
A CLI expense tracking app with session-based SQLite storage.
- Create expense sessions with multiple entries
- View session summaries with totals and item counts
- Auto-creates `expenses.db` on first run

```bash
python project_2/expense_tracker.py
```

### Project 3: Secure Password Generator (`project_3/`)
A CLI password generator using `secrets` library for cryptography randomness with real-time strength estimation.

#### Features
- **Length validation:** prompts for length (15–64 recommended per NIST 2024), warns on short inputs with override option
- **Punctuation toggle:** ask whether to include `string.punctuation` (32 special characters) in the character pool
- **Cryptographic randomness:** uses `secrets.choice()` instead of `random.choice()`
- **Strength estimation summary:**
  - Entropy in bits: `length × log₂(pool_size)`
  - Total possibilities: `pool_size^length`
  - Estimated crack time at 10⁹ guesses/s formatted in human readable values

#### Example run
```
Random password generator
Enter password length: 16
Include punctuation? (y/n): y

Password: aB3#kL9$xQ2@vR7&
Length: 16 characters
Entropy: 98.32 bits
Possibilities: 94^16 = 3.72e31
Crack time: 117.8 trillion centuries
```

#### Character pools
| Characters | Pool size | Source                       |
|------------|-----------|------------------------------|
| Letters + digits | 62 | `string.ascii_letters` + `string.digits` |
| + Punctuation    | 94 | + `string.punctuation`      |

```bash
python project_3/random_password_generator.py
```

## Requirements

- Python 3.x
- SQLite3 (standard library)

