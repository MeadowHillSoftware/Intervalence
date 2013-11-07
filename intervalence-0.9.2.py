#!/usr/bin/env python

# Intervalence 0.9.2
# Copyright 2009-2010 Meadow Hill Software
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygtk
pygtk.require("2.0")
import gtk
from random import randrange

#notes: c, c#/db, d, d#/eb, e, f, f#/gb, g, g#/ab, a, a#/bb, b
#intervals: m2/m9, M2/M9, m3, M3, P4/P11, A4/A11, d5, P5, A5, m6, M6/M13, d7, m7, M7
degrees = ["C", "D", "E", "F", "G", "A", "B"]
directions = ["up", "down"]
keyboard = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
notes = {1: ["B#", "C", "Dbb"], 2: ["Bx", "C#", "Db"], 3: ["Cx", "D", "Ebb"], 4: ["D#", "Eb", "Fbb"], 5: ["Dx", "E", "Fb"], 6: ["E#", "F", "Gbb"], 7: ["Ex", "F#", "Gb"], 8: ["Fx", "G", "Abb"], 9: ["G#", "Ab"], 10: ["Gx", "A", "Bbb"], 11: ["A#", "Bb", "Cbb"], 12: ["Ax", "B", "Cb"]}
intervals = ["m2", "M2", "m3", "M3", "P4", "A4", "d5", "P5", "A5", "m6", "M6", "d7", "m7", "M7", "m9", "M9", "A9", "P11", "M13"]
halves = {"m2": 1, "M2": 2, "m3": 3, "M3": 4, "P4": 5, "A4": 6, "d5": 6, "P5": 7, "A5": 8, "m6": 8, "M6": 9, "d7": 9, "m7": 10, "M7": 11, "m9": 13, "M9": 14, "A9": 15, "P11": 17, "A11": 18, "M13": 21}

def createButton(label):
	button = gtk.Button(label)
	button.show()
	return button

class Tester():
	def __init__(self):
		self.window = gtk.Dialog("~Intervalence~")
		self.window.connect("delete_event", gtk.main_quit, False)
		self.grade = createButton("Grade")
		self.window.action_area.pack_start(self.grade, True, True, 0)
		self.grade.connect_object("clicked", self.gradeUser, None)
		self.quit = createButton("Quit")
		self.window.action_area.pack_start(self.quit, True, True, 0)
		self.quit.connect_object("clicked", gtk.main_quit, False)
		self.table = gtk.Table(6, 6)
		self.window.vbox.pack_start(self.table, False, False, 0)
		self.table2 = gtk.Table(6, 5)
		self.min2 = gtk.CheckButton("Minor 2nd")
		self.maj2 = gtk.CheckButton("Major 2nd")
		self.min3 = gtk.CheckButton("Minor 3rd")
		self.maj3 = gtk.CheckButton("Major 3rd")
		self.p4 = gtk.CheckButton("Perfect 4th")
		self.a4 = gtk.CheckButton("Augmented 4th")
		self.d5 = gtk.CheckButton("Diminished 5th")
		self.p5 = gtk.CheckButton("Perfect 5th")
		self.a5 = gtk.CheckButton("Augmented 5th")
		self.min6 = gtk.CheckButton("Minor 6th")
		self.maj6 = gtk.CheckButton("Major 6th")
		self.d7 = gtk.CheckButton("Diminished 7th")
		self.min7 = gtk.CheckButton("Minor 7th")
		self.maj7 = gtk.CheckButton("Major 7th")
		self.min9 = gtk.CheckButton("Minor 9th")
		self.maj9 = gtk.CheckButton("Major 9th")
		self.a9 = gtk.CheckButton("Augmented 9th")
		self.p11 = gtk.CheckButton("Perfect 11th")
		self.maj13 = gtk.CheckButton("Major 13th")
		self.all2 = gtk.CheckButton("2nds")
		self.all3 = gtk.CheckButton("3rds")
		self.all4 = gtk.CheckButton("4ths")
		self.all5 = gtk.CheckButton("5ths")
		self.all6 = gtk.CheckButton("6ths")
		self.all7 = gtk.CheckButton("7ths")
		self.all9 = gtk.CheckButton("9ths")
		self.simple = gtk.CheckButton("Simple Intervals")
		self.compound = gtk.CheckButton("Compound Intervals")
		self.all = gtk.CheckButton("All Intervals")
		self.clear = createButton("Clear")
		self.min2.connect("toggled", self.checkIntervals, None)
		self.maj2.connect("toggled", self.checkIntervals, None)
		self.min3.connect("toggled", self.checkIntervals, None)
		self.maj3.connect("toggled", self.checkIntervals, None)
		self.p4.connect("toggled", self.checkIntervals, None)
		self.a4.connect("toggled", self.checkIntervals, None)
		self.d5.connect("toggled", self.checkIntervals, None)
		self.p5.connect("toggled", self.checkIntervals, None)
		self.a5.connect("toggled", self.checkIntervals, None)
		self.min6.connect("toggled", self.checkIntervals, None)
		self.maj6.connect("toggled", self.checkIntervals, None)
		self.d7.connect("toggled", self.checkIntervals, None)
		self.min7.connect("toggled", self.checkIntervals, None)
		self.maj7.connect("toggled", self.checkIntervals, None)
		self.min9.connect("toggled", self.checkIntervals, None)
		self.maj9.connect("toggled", self.checkIntervals, None)
		self.a9.connect("toggled", self.checkIntervals, None)
		self.p11.connect("toggled", self.checkIntervals, None)
		self.maj13.connect("toggled", self.checkIntervals, None)
		self.all2.connect("toggled", self.checkIntervals, None)
		self.all3.connect("toggled", self.checkIntervals, None)
		self.all4.connect("toggled", self.checkIntervals, None)
		self.all5.connect("toggled", self.checkIntervals, None)
		self.all6.connect("toggled", self.checkIntervals, None)
		self.all7.connect("toggled", self.checkIntervals, None)
		self.all9.connect("toggled", self.checkIntervals, None)
		self.simple.connect("toggled", self.checkIntervals, None)
		self.compound.connect("toggled", self.checkIntervals, None)
		self.all.connect("toggled", self.checkIntervals, None)
		self.clear.connect("clicked", self.checkIntervals, None)
		self.table2.attach(self.min2, 0, 1, 0, 1)
		self.table2.attach(self.maj2, 0, 1, 1, 2)
		self.table2.attach(self.min3, 0, 1, 2, 3)
		self.table2.attach(self.maj3, 0, 1, 3, 4)
		self.table2.attach(self.p4, 0, 1, 4, 5)
		self.table2.attach(self.a4, 0, 1, 5, 6)
		self.table2.attach(self.d5, 1, 2, 0, 1)
		self.table2.attach(self.p5, 1, 2, 1, 2)
		self.table2.attach(self.a5, 1, 2, 2, 3)
		self.table2.attach(self.min6, 1, 2, 3, 4)
		self.table2.attach(self.maj6, 1, 2, 4, 5)
		self.table2.attach(self.d7, 1, 2, 5, 6)
		self.table2.attach(self.min7, 2, 3, 0, 1)
		self.table2.attach(self.maj7, 2, 3, 1, 2)
		self.table2.attach(self.min9, 2, 3, 2, 3)
		self.table2.attach(self.maj9, 2, 3, 3, 4)
		self.table2.attach(self.a9, 2, 3, 4, 5)
		self.table2.attach(self.p11, 2, 3, 5, 6)
		self.table2.attach(self.maj13, 3, 4, 0, 1)
		self.table2.attach(self.all2, 3, 4, 1, 2)
		self.table2.attach(self.all3, 3, 4, 2, 3)
		self.table2.attach(self.all4, 3, 4, 3, 4)
		self.table2.attach(self.all5, 3, 4, 4, 5)
		self.table2.attach(self.all6, 3, 4, 5, 6)
		self.table2.attach(self.all7, 4, 5, 0, 1)
		self.table2.attach(self.all9, 4, 5, 1, 2)
		self.table2.attach(self.simple, 4, 5, 2, 3)
		self.table2.attach(self.compound, 4, 5, 3, 4)
		self.table2.attach(self.all, 4, 5, 4, 5)
		self.table2.attach(self.clear, 4, 5, 5, 6)
		self.table.attach(self.table2, 0, 6, 0, 1)
		self.label = gtk.Label("")
		self.table.attach(self.label, 0, 6, 1, 2)
		self.separator = gtk.HSeparator()
		self.table.attach(self.separator, 0, 6, 2, 3)
		self.label = gtk.Label("")
		self.table.attach(self.label, 0, 6, 3, 4)
		self.article = gtk.Label("An   ")
		self.table.attach(self.article, 0, 1, 4, 5)
		self.interval = gtk.combo_box_new_text()
		self.table.attach(self.interval, 1, 2, 4, 5)
		self.interval.append_text("INTERVAL")
		self.interval.append_text("Minor 2nd")
		self.interval.append_text("Major 2nd")
		self.interval.append_text("Minor 3rd")
		self.interval.append_text("Major 3rd")
		self.interval.append_text("Perfect 4th")
		self.interval.append_text("Augmented 4th")
		self.interval.append_text("Diminished 5th")
		self.interval.append_text("Perfect 5th")
		self.interval.append_text("Augmented 5th")
		self.interval.append_text("Minor 6th")
		self.interval.append_text("Major 6th")
		self.interval.append_text("Diminished 7th")
		self.interval.append_text("Minor 7th")
		self.interval.append_text("Major 7th")
		self.interval.append_text("Minor 9th")
		self.interval.append_text("Major 9th")
		self.interval.append_text("Augmented 9th")
		self.interval.append_text("Perfect 11th")
		self.interval.append_text("Augmented 11th")
		self.interval.append_text("Major 13th")
		self.interval.set_active(0)
		self.interval.connect("changed", self.generateQuestion, None)
		self.phrase = gtk.Label("   <direction> from <note> is   ")
		self.table.attach(self.phrase, 2, 3, 4, 5)
		self.letter = gtk.combo_box_new_text()
		self.table.attach(self.letter, 3, 4, 4, 5)
		self.letter.append_text("LETTER")
		self.letter.append_text("A")
		self.letter.append_text("B")
		self.letter.append_text("C")
		self.letter.append_text("D")
		self.letter.append_text("E")
		self.letter.append_text("F")
		self.letter.append_text("G")
		self.letter.set_active(0)
		self.accidental = gtk.combo_box_new_text()
		self.table.attach(self.accidental, 4, 5, 4, 5)
		self.accidental.append_text("ACCIDENTAL")
		self.accidental.append_text("Double-Flat")
		self.accidental.append_text("Flat")
		self.accidental.append_text("Natural")
		self.accidental.append_text("Sharp")
		self.accidental.append_text("Double-Sharp")
		self.accidental.set_active(0)
		self.enter = createButton("Enter")
		self.enter.connect("clicked", self.checkAnswer, None)
		self.table.attach(self.enter, 5, 6, 4, 5)
		self.scrolledwindow = gtk.ScrolledWindow()
		self.scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.table.attach(self.scrolledwindow, 0, 6, 5, 6)
		self.results = gtk.TextView()
		self.scrolledwindow.add(self.results)
		self.results.set_wrap_mode(gtk.WRAP_WORD)
		self.results.set_justification(gtk.JUSTIFY_LEFT)
		self.results.set_editable(False)
		self.results.set_cursor_visible(False)
		self.results_buffer = self.results.get_buffer()
		self.correct = ""
		self.total = 0
		self.right = 0
		self.window.show_all()

	def checkAnswer(self, widget, data = None):
		interval = self.getEntry(self.interval)
		letter = self.getEntry(self.letter)
		accidental = self.getEntry(self.accidental)
		if interval == "INTERVAL":
			self.selectInterval()
			return None
		if letter == "LETTER" or accidental == "ACCIDENTAL":
			if len(self.correct) > 1:
				note = self.correct[0]
				accidental = self.correct[1:]
				accidentals = {"bb": "Double-Flat", "b": "Flat", "#": "Sharp", "x": "Double-Sharp"}
				accidental = accidentals[accidental]
				correct = note + " " + accidental
			else:
				correct = self.correct
			beginning = self.article.get_text()[:-3]
			phrase = self.phrase.get_text()[3:-3]
			feedback = "Incorrect.  %s %s %s %s." % (self.article.get_text(), self.getEntry(self.interval), phrase, self.correct)
		else:
			accidentals = {"Double-Flat": "bb", "Flat": "b", "Natural": "", "Sharp": "#", "Double-Sharp": "x"}
			accidental = accidentals[accidental]
			answer = letter + accidental
			if answer == self.correct:
				feedback = "Correct.  Good job."
				self.right += 1
			else:
				if len(self.correct) > 1:
					note = self.correct[0]
					accidental = self.correct[1:]
					accidentals = {"bb": "Double-Flat", "b": "Flat", "#": "Sharp", "x": "Double-Sharp"}
					accidental = accidentals[accidental]
					correct = note + " " + accidental
				else:
					correct = self.correct
				beginning = self.article.get_text()[:-3]
				phrase = self.phrase.get_text()[3:-3]
				feedback = "Incorrect.  %s %s %s %s." % (self.article.get_text(), self.getEntry(self.interval), phrase, self.correct)
		self.results_buffer.set_text(feedback)
		self.total += 1
		self.generateQuestion(self.interval, data = None)

	def checkIntervals(self, widget, data = None):
		button_list = ()
		interval_buttons = [self.min2, self.maj2, self.min3, self.maj3, self.p4, self.a4, self.d5, self.p5, self.a5, self.min6, self.maj6, self.d7, self.min7, self.maj7, self.min9, self.maj9, self.a9, self.p11, self.maj13]
		simple_buttons = [self.min2, self.maj2, self.min3, self.maj3, self.p4, self.a4, self.d5, self.p5, self.a5, self.min6, self.maj6, self.d7, self.min7, self.maj7]
		compound_buttons = [self.min9, self.maj9, self.a9, self.p11, self.maj13]
		all2_buttons = [self.min2, self.maj2]
		all3_buttons = [self.min3, self.maj3]
		all4_buttons = [self.p4, self.a4]
		all5_buttons = [self.d5, self.p5, self.a5]
		all6_buttons = [self.min6, self.maj6]
		all7_buttons = [self.d7, self.min7, self.maj7]
		all9_buttons = [self.min9, self.maj9, self.a9]
		set_buttons = [self.all, self.simple, self.compound, self.all2, self.all3, self.all4, self.all5, self.all6, self.all7, self.all9]
		button_dic = {self.all: interval_buttons, self.simple: simple_buttons, self.compound: compound_buttons, self.all2: all2_buttons, self.all3: all3_buttons, self.all4: all4_buttons, self.all5: all5_buttons, self.all6: all6_buttons, self.all7: all7_buttons, self.all9: all9_buttons}
		if widget in set_buttons:
			if widget.get_active():
				button_list = button_dic[widget]
				for button in button_list:
					button.set_active(True)
		elif widget == self.clear:
			for button in interval_buttons:
				button.set_active(False)
			for button in set_buttons:
				button.set_active(False)

	def generateQuestion(self, widget, data = None):
		self.selectInterval()
		interval = self.getEntry(self.interval)
		letter = interval[0]
		if letter != "I":
			key = keyboard[randrange(0, 17)]
			direction = directions[randrange(0, 2)]
			if letter == "A":
				article = "An"
			else:
				article = "A"
		else:
			article = "An"
			key = "<note>"
		self.article.set_text(article)
		if len(key) < 3:
			if len(key) == 2:
				if key[1] == "b":
					note = key[0] + " Flat"
				else:
					note = key[0] + " Sharp"
			else:
				note = key[0]
			slice = interval[:-2]
			quality, quantity = slice.split(" ")
			if quality in ["Minor", "Diminished"]:
				letter = letter.lower()
			interval =  letter + quantity
			span = int(quantity)
			moves = span - 1
			start = degrees.index(key[:1])
			if direction == "up":
				end = start + moves
			else:
				end = start - moves
			while end > 6:
				end -= 7
			while end < 0:
				end += 7
			degree = degrees[end]
			steps = halves[interval]
			for num in notes.keys():
				if key in notes[num]:
					rootnum = num
			if direction == "up":
				finish = rootnum + steps
			else:
				finish = rootnum - steps
			while finish > 12:
				finish -= 12
			while finish < 1:
				finish += 12
			for enharmonic in notes[finish]:
				if degree in enharmonic:
					self.correct = enharmonic[:]
		else:
			note = key[:]
			direction = "<direction>"
		phrase = "   %s from %s is   " % (direction, note)
		article = article + "   "
		self.phrase.set_text(phrase)

	def getEntry(self, data):
		model = data.get_model()
		index = data.get_active()
		if index < 0:
			return None
		return model[index][0]

	def gradeUser(self, widget, data = None):
		wrong = self.total - self.right
		breakdown = "Total Questions: %d\n\nCorrect Answers: %d\n\nIncorrect Answers: %d\n\n" % (self.total, self.right, wrong)
		right = float(self.right) * 100
		percentage = right / float(self.total)
		if percentage >= 90.0:
			category = "Excellent.\n\n"
		elif percentage >= 80.0:
			category = "Above Average.\n\n"
		elif percentage >= 70.0:
			category = "Average.\n\n"
		elif percentage >= 60.0:
			category = "Below Average.\n\n"
		else:
			category = "Poor.\n\n"
		remarks = "%s%sYou got %d percent correct." % (breakdown, category, percentage)
		self.results_buffer.set_text(remarks)

	def selectInterval(self):
		interval_buttons = [self.min2, self.maj2, self.min3, self.maj3, self.p4, self.a4, self.d5, self.p5, self.a5, self.min6, self.maj6, self.d7, self.min7, self.maj7, self.min9, self.maj9, self.a9, self.p11, self.maj13]
		interval_dic = {self.min2: 1, self.maj2: 2, self.min3: 3, self.maj3: 4, self.p4: 5, self.a4: 6, self.d5: 7, self.p5: 8, self.a5: 9, self.min6: 10, self.maj6: 11, self.d7: 12, self.min7: 13, self.maj7: 14, self.min9: 15, self.maj9: 16, self.a9: 17, self.p11: 18, self.maj13: 19}
		test_intervals = [button for button in interval_buttons if button.get_active()]
		if len(test_intervals) < 1:
			return None
		else:
			num = randrange(0, len(test_intervals))
			button = test_intervals[num]
			num = interval_dic[button]
			self.interval.set_active(num)

def main():
	gtk.main()

if __name__ == "__main__":
	tester = Tester()
	main()
