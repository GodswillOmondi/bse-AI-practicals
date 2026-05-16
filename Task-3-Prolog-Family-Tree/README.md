# TASK THREE – PROLOG

## Objective

This assignment demonstrates:

1. Downloading and configuring Prolog
2. Running basic Prolog logic programs
3. Creating a family tree using Prolog facts and rules

---

# Step 1: Download and Configure Prolog

The Prolog distribution used in this assignment is:

- SWI-Prolog

Official website:

https://www.swi-prolog.org/

## Installation Steps

### Ubuntu/Linux

```bash
sudo apt update
sudo apt install swi-prolog
```

### Windows

1. Download SWI-Prolog from the official website
2. Run the installer
3. Finish installation
4. Launch SWI-Prolog

---

# Step 2: Running Prolog Programs

Start Prolog:

```bash
swipl
```

Load the family program:

```prolog
['family.pl'].
```

Expected output:

```prolog
true.
```

---

# Step 3: Family Tree Implementation

The family tree contains:

- Grandparents
- Parents
- Children
- Grandchildren
- Cousins
- Uncles
- Aunts

---

# Example Queries

## Parent Query

```prolog
?- parent(john, michael).
```

Output:

```prolog
true.
```

---

## Grandparent Query

```prolog
?- grandparent(john, david).
```

Output:

```prolog
true.
```

---

## Cousin Query

```prolog
?- cousin(david, james).
```

Output:

```prolog
true.
```

---

## Uncle Query

```prolog
?- uncle(michael, james).
```

Output:

```prolog
true.
```

---

# Files Included

- family.pl → Prolog family tree program
- README.md → Assignment explanation
- screenshots → Program execution screenshots

---

# Conclusion

This assignment successfully demonstrated the installation and configuration of Prolog, execution of basic logic programs, and implementation of a family tree using facts and logical rules.
