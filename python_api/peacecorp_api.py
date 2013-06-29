# -*- coding: utf-8 -*-

# peace corp app api demo
# Copyright 2013 Sean Fahey

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
from werkzeug import secure_filename
import os
import MySQLdb, json

# configuration
DEBUG = True
host = 'xxx'
user = 'xxx'
password = 'xxx'
database = 'xxx'
table = 'xxx'

def get_json(query):

	con = MySQLdb.connect(host, user, password, database)

	with con:
		cur = con.cursor()
		cur.execute(query)
		rows = cur.fetchall()

		rowarray = []
		for row in rows:
			_URI = str(row[0])
			_CREATOR_URI_USER = str(row[1])
			_CREATION_DATE = str(row[2])
			_LAST_UPDATE_URI_USER = str(row[3])
			_LAST_UPDATE_DATE = str(row[4])
			_MODEL_VERSION = str(row[5])
			_UI_VERSION = str(row[6])
			_IS_COMPLETE = str(row[7])
			_SUBMISSION_DATE = str(row[8])
			_MARKED_AS_COMPLETE_DATE = str(row[9])
			META_INSTANCE_ID = str(row[10])
			INTRO_PROJ_DATE_END = str(row[11])
			PARTNERS_PARTNERS = str(row[12])
			INTRO_VOL_NAME = str(row[13])
			INTRO_PROJECT_DATE_START = str(row[14])
			PARTNERS_VOLUNTEERS = str(row[15])
			LOCATION_GEOLOCATION_LNG = str(row[16])
			LOCATION_GEOLOCATION_ACC = str(row[17])
			PARTICIPANTS_FEMALE_18ANDOVER = str(row[18])
			SECTORS_INITIATIVE = str(row[19])
			PARTICIPANTS_FEMALE_UNDER13 = str(row[20])
			LOCATION_GEOLOCATION_LAT = str(row[21])
			PARTICIPANTS_MALE_UNDER13 = str(row[22])
			LOCATION_LOCATION = str(row[23])
			PARTICIPANTS_MALE_13TO17 = str(row[24])
			LOCATION_GEOLOCATION_ALT = str(row[25])
			SKILLS_INVOLVED = str(row[26])
			NOTES = str(row[27])
			PARTICIPANTS_MALE_18ANDOVER = str(row[28])
			PARTICIPANTS_FEMALE_13TO17 = str(row[29])

			t = (_URI,_CREATOR_URI_USER,_CREATION_DATE,_LAST_UPDATE_URI_USER,_LAST_UPDATE_DATE,_MODEL_VERSION,_UI_VERSION,_IS_COMPLETE,_SUBMISSION_DATE,_MARKED_AS_COMPLETE_DATE,META_INSTANCE_ID,INTRO_PROJ_DATE_END,PARTNERS_PARTNERS,INTRO_VOL_NAME,INTRO_PROJECT_DATE_START,PARTNERS_VOLUNTEERS,LOCATION_GEOLOCATION_LNG,LOCATION_GEOLOCATION_ACC,PARTICIPANTS_FEMALE_18ANDOVER,SECTORS_INITIATIVE,PARTICIPANTS_FEMALE_UNDER13,LOCATION_GEOLOCATION_LAT,PARTICIPANTS_MALE_UNDER13,LOCATION_LOCATION,PARTICIPANTS_MALE_13TO17,LOCATION_GEOLOCATION_ALT,SKILLS_INVOLVED,NOTES,PARTICIPANTS_MALE_18ANDOVER,PARTICIPANTS_FEMALE_13TO17)
			rowarray.append(t)

		j = json.dumps(rowarray)

	return j

# application
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	return "Hello, World!"

@app.route('/notebooks')
def notebooks():
	return str(get_json('SELECT * FROM ' + table))

@app.route('/notebooks/<username>')
def by_username(username):
	return str(get_json('SELECT * FROM ' + table + ' WHERE _CREATOR_URI_USER = "%s"' % (username)))

if __name__ == '__main__':
    #init_db()
    app.run(host='0.0.0.0')
