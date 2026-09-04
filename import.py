import streamlit as st
a=st.chat_input("enter command")
if a:
	st.chat_message("user").write(a)
	if a.lower()=="hi":
		st.chat_message("ai",avatar="bot.png").write("hello")
	elif a.lower()=="age":
		st.chat_message("ai",avatar="bot.png").write("20")
	elif a.lower()=="date of birth":
		st.chat_message("ai",avatar="bot.png").write("29-07-2006")
	elif a.lower()=="college": 
		st.chat_message("ai",avatar="bot.png").write("ssmrv")
	elif a.lower()=="course":
		st.chat_message("ai",avatar="bot.png").write("bca") 
	elif a.lower()=="skill":
		st.chat_message("ai",avatar="bot.png").write("python")
	elif a.lower()=="exit": 
		st.chat_message("ai",avatar="bot.png").write("session stopped")

