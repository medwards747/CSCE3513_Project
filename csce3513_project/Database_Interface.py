
from supabase import create_client, Client
import Page




class Database_Interface:
    url = "https://wceblbcdgfoqocminldo.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndjZWJsYmNkZ2ZvcW9jbWlubGRvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzYzMTg5MDUsImV4cCI6MTk5MTg5NDkwNX0.b15JOIrzQJM_hyHJN1-TdDZQb25zRuRp32ybMW4l5hw"
    supabase: Client = create_client(url, key)

    def searchID(self, id):
        result = self.supabase.table("player").select("*").eq("id",id).execute().data
        if result == []:
            return(False)
        else:
            return(result)
    
    #insertName expects a dictionary containing
    #id, codename, last_name, first_name

    def insertName(self,dict):
        self.supabase.table("player").insert(dict).execute()
    








        

