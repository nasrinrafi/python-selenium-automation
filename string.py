class Info:
   def _int_(self,first_name ,last_name):
      first_name= self.first_name
      last_name=self.last_name

   def __str__(self):
    return f"{self.first_name}{self.last_name}"
   def __repr__(self):
       return f"{self.fist_name}{self.last_name}"


Info =("nasrin","rafi")
f"{Info}"
