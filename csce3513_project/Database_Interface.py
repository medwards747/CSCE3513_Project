
from supabase import create_client, Client


class Database_Interface:
    url = "https://gmqxbfvbtseyxorhjfct.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdtcXhiZnZidHNleXhvcmhqZmN0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyMzA1MDYsImV4cCI6MTk5NjgwNjUwNn0.cH9g_PM6S845tTKfvUZrlu6UeEYB9lMYnPBXAlQOSaY"
    supabase: Client = create_client(url, key)

    def searchID(self, id):
        result = self.supabase.table("player").select("*").eq("id",id).explain().execute().data
        if result == []:
            return(False)
        else:
            return(result)
    
    #insertName expects a dictionary containing
    #id, codename, last_name, first_name
    #keys should be strings containing exactly the above

    def insertName(self,dict):
        self.supabase.table("player").insert(dict).execute()
    








        

