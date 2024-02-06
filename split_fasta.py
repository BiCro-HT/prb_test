from Bio import SeqIO
ref_genome = './data/ref/GCF_009914755.1_T2T-CHM13v2.0_genomic.fna'

identifier = []
sequence = []
for record in SeqIO.parse(ref_genome, "fasta"):
    identifier.append(record.id)
    sequence = str(record.seq)

print("\n".join(identifier))
print(len(identifier))