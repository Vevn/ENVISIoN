#
#  ENVISIoN
#
#  Copyright (c) 2019 Jesper Ericcson
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##############################################################################################
#
#  Alterations to this file by Anton Hjert
#
#  To the extent possible under law, the person who associated CC0
#  with the alterations to this file has waived all copyright and related
#  or neighboring rights to the alterations made to this file.
#
#  You should have received a copy of the CC0 legalcode along with
#  this work.  If not, see
#  <http://creativecommons.org/publicdomain/zero/1.0/>.

import wx, sys, os

class GeneralCollapsible(wx.CollapsiblePane):

    # Initialize with parent pane and desired label-string
    def __init__(self, parent, label):
        super().__init__(parent, label = label)

        # Set the style of the pane
        self.bg_colour = wx.Colour(130,130,130)
        self.text_colour = wx.Colour(255,255,255)
        self.itemSize = wx.Size(150,25)

        self.SetBackgroundColour(self.bg_colour)

        self.pane = self.GetPane()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.pane.SetSizer(self.sizer)
        
    
        # Default callback when collapsing panel, just updates the layouts to make sizers expand
        # Can freely be changed in subclasses, just make sure to call update_layout there aswell
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.on_collapse)

        self.parent_collapsible = None
        self.sub_collapsibles = []

    def add_item(self, item, sizer_flags = wx.SizerFlags().Expand().Border(wx.ALL, 0)):
        # Add some wx widged to the expandible panel
        self.sizer.Add(item, sizer_flags)

    def add_sub_collapsible(self, item):
        # Add a collapsible panel
        self.sizer.Add(item)
        self.sub_collapsibles.append(item)
        item.parent_collapsible = self

    def collapse_children(self):
        for collapsible in self.sub_collapsibles:
            collapsible.Collapse(True)
            collapsible.on_collapse(event = None)

    def on_collapse(self, event = None):
        # Default collapse callback, only updates layout
        # Binding can be changed in sub-classes
        self.update_collapse()


    def update_collapse(self, event = None):
        # Function to handle things that need to be done after
        # toggling collapse.

        # Updates the layout of the collapsible
        # Collapses children if needed
        # Fixes the size of things look correct after collapse

        # If collapsed collapse all sub collapsibles
        if self.IsCollapsed():
            self.collapse_children()
            
        # For some reason this makes the sub panels expand correctly
        # Seems to be needed on linux, can maybe be simplified tho.
        if self.parent_collapsible != None:
            self.parent_collapsible.Collapse(not self.parent_collapsible.IsCollapsed())
            self.parent_collapsible.Collapse(not self.parent_collapsible.IsCollapsed())
            self.parent_collapsible.Layout()
            # self.parent_collapsible.update_collapse()

        # Update the layout of parent widgets
        self.Layout()
        widget = self
        while True:
         widget = widget.GetParent()
         widget.Layout()
         if widget.IsTopLevel():
             break