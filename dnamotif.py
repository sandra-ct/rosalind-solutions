# rosalind - finding a motif in DNA

import regex as re

with open (r"rosalind_subs.txt", 'r') as file:
    content = file.read()
seq_raw, sub_seq = content.splitlines() # seq = s, sub_seq = t

seq = re.sub(' ', '', seq_raw)

sub_locs = re.finditer(sub_seq,seq)
matches = [sub.group() for sub in sub_locs]

search_loc = re.search(sub_seq,seq)
start_end_locations = [search.span() for search in re.finditer(sub_seq,seq)]

all_iterations = [sub.start(0) for sub in re.finditer(sub_seq,seq)]

print('Full Seq:\n', seq, '\nSearching for: ', sub_seq, '\n\nMatched Strings:', matches, '\n\n', 'Span of Matches:', start_end_locations, '\n\n', 'Locations of All Matches:', all_iterations)
