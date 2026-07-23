from codingquiz import total_fines
def test_zerofine():
    fine=[]
    assert total_fines(fine)=="The Total Fines of the Library is $0.00"
def test_somefine():
    ab=[1,6,8,4,6.7]
    assert total_fines(ab)=="The Total Fines of the Library is $25.70"

from codingquiz import Fine
def test_aboveten():
    fine=Fine("dune","abdul.rafey.1857@gmail.com",45)
    assert fine.amount==10
def test_belowten():
    fine2=Fine("dune","abdul.rafey.1857@gmail.com",35)
    assert fine2.amount==8.75

   