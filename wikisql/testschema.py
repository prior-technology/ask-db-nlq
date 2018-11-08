import unittest
from schema import build_schema
import graphene
#test schema without mutations ...
class TestSchema(unittest.TestCase):
  def setUp(self):
    (rootQueryClass,mutationsClass) = build_schema('/home/stevop/repos/coarse2fine/data_model/wikisql/data')
    self.schema = graphene.Schema(query=rootQueryClass, mutation=mutationsClass)
    #need to init a fake engine
    
  def test_mutation(self):
    result = self.schema.execute("""mutation m {
    askQuestion(tableId:"1-10015132-11", questionText: "How many years did Brad play for Toronto") 
    {
        sql
    }
}""")
    print(result.data['sql'])
    self.assertEqual('SELECT  col4 FROM table WHERE col5 = Brad', result.data['sql'])

  def test_query(self):
    result = self.schema.execute("""{"query":"{ tables {id, tablename }}"}""")
    print(result.data['sql'])

if __name__ == '__main__':
    unittest.main()
