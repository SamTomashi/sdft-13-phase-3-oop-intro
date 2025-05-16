
'''
1. One coworking space where people share a single printer: 1 printer, 1 office, many documents
2. A company with different offices sharing one printe: 1 printer, many offices, many documents
'''
class Document:
   def __init__(self, title):
       self.title = title
   

class Printer:
    def print_document(self, document):
        print(f"Printing: {document.title}")

class Office:
    def do_printing(self, doc_title):
        document = Document(doc_title) # document that the user is printing

        kyocera = Printer() # printer being used
        kyocera.print_document(document)


class ServerRoom:
      def do_printing(self, doc_title):
        document = Document(doc_title) # document that the user is printing

        laser_printer = Printer() # printer being used
        laser_printer.print_document(document)


office = Office()
office.do_printing("project_plan.pdf")


server_room = ServerRoom()
server_room.do_printing("procurment of new computers.pdf")
