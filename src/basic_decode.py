import py_qcode as pq
import networkx as nx
from qecc import X, Z, I

#size=(4,4)
#size=(40,40)
size=(2,2)

'''
test_lattice = pq.SquareLattice(size)
test_dual_lattice = pq.SquareLattice(size, is_dual=True)
test_model = pq.depolarizing_model(0.05)
test_code = pq.toric_code(test_lattice, test_dual_lattice)
test_decoder = pq.mwpm_decoder(test_lattice, test_dual_lattice)
test_logical_ops = pq.toric_log_ops(test_lattice.size)
'''

test_lattice = pq.SquareOctagonLattice(size)
test_dual_lattice = pq.UnionJackLattice(size, is_dual=True)
test_model = pq.depolarizing_model(0.05)
test_code = pq.square_octagon_code(test_lattice, test_dual_lattice)
test_decoder = pq.mwpm_decoder(test_lattice, test_dual_lattice)
test_logical_ops = pq.squoct_log_ops(test_lattice.total_size)

test_model.act_on(test_lattice)
print "Real Errors: \n============"
pq.error_print(test_lattice)

test_code.measure()
print "Syndromes: \n=========="
pq.syndrome_print(test_dual_lattice)

test_decoder.infer()
print "Error After Decoding:\n====================="
pq.error_print(test_lattice)

test_code.measure()
print "Syndromes After Decoding:\n========================="
pq.syndrome_print(test_lattice)

print "Logical Operators:\n=================="
for op in test_logical_ops:
    print op.pauli

print "Logical Operator Commutation Relations:\n======================================="
for op in test_logical_ops:
    print op.test(test_lattice)
