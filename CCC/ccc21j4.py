books = input()
L = books.count("L")
M = books.count("M")
S = books.count("S")

L_section = books[:L]     # all books in L section
M_section = books[L:L+M]  # all books in M section
S_section = books[L+M:]   # all books in S section

M_L = L_section.count("M")  # M book in the L section
S_L = L_section.count("S")
L_M = M_section.count("L")
S_M = M_section.count("S")
L_S = S_section.count("L")
M_S = S_section.count("M")

M_L_swap = min(M_L, L_M)  # this is the direct swap
M_L -= M_L_swap   # don't forget to remove the number
L_M -= M_L_swap
S_L_swap = min(S_L, L_S)
S_L -= S_L_swap
L_S -= S_L_swap
M_S_swap = min(M_S, S_M)
M_S -= M_S_swap
S_M -= M_S_swap

print(M_L_swap + S_L_swap + M_S_swap + 2 * M_L + 2 * S_L)