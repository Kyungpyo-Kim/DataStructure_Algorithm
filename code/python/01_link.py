class Link:
  def __init__(self, d1=None, d2=None):
    self.data1 = d1
    self.data2 = d2
    self.next_link = None

  def printLink(self):
    print ( "{", self.data1, ", ", self.data2, "}")

class LinkList:
  def __init__(self):
    self.first_link = None

  def isEmpty(self):
	  return self.first_link == None

  def insert(self, d1, d2):
    if self.first_link == None : 
      self.first_link = Link( d1, d2 )
    else:
      tmp_next_link = self.first_link
      self.first_link = Link( d1, d2 )
      # first_link 의 next_link 초기화됨
      self.first_link.next_link = tmp_next_link
      
  def delete(self):
    rlink = self.first_link
    self.first_link = self.first_link.next_link
    return rlink
	
  def printList(self):
      curLink = self.first_link
      print ( "Link list" )
      while(curLink != None):
          curLink.printLink()
          curLink = curLink.next_link

def test():
  link_list = LinkList()
  link_list.insert( 1, 100 )
  link_list.insert( 2, 200 )
  link_list.insert( 3, 300 )
  link_list.insert( 4, 400 )
  link_list.insert( 5, 500 )
  
  link_list.printList()

  while( not link_list.isEmpty() ):
      deletedLink = link_list.delete()
      print ( "delete" )
      deletedLink.printLink()
      
  link_list.printList()

test()
