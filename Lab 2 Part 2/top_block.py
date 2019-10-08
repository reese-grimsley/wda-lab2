#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: WDA Channel Simulator v2
# Author: Cef Ramirez
# Generated: Tue Oct  8 08:58:48 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import numpy
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "WDA Channel Simulator v2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("WDA Channel Simulator v2")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 200
        self.excess_bw = excess_bw = 0.35
        self.QAM = QAM = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base()
        self.symbol_reflection_offset = symbol_reflection_offset = 0
        self.symbol_reflection_ampl = symbol_reflection_ampl = 0
        self.samp_rate = samp_rate = 1e6
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(1, sps, 1, excess_bw, 45)
        self.refl_delay = refl_delay = 0
        self.refl_amplitude = refl_amplitude = 0
        self.noise_level = noise_level = 0
        self.max_phase_offset_ratio = max_phase_offset_ratio = 1
        self.direct_amplitude = direct_amplitude = 1
        self.constellation = constellation = QAM
        self.carrier_frequency = carrier_frequency = 10e3
        self.bits_per_symbol = bits_per_symbol = 2
        self.PSK = PSK = digital.constellation_calcdist(([1+0j, -1+0j]), ([0, 1]), 2, 1).base()

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, "Time")
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, "Frequency")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "Windowed Constellation")
        self.top_grid_layout.addWidget(self.tab, 0,0,1,7)
        self._symbol_reflection_offset_range = Range(0, 1, 0.01, 0, 100)
        self._symbol_reflection_offset_win = RangeWidget(self._symbol_reflection_offset_range, self.set_symbol_reflection_offset, "Offset (% of Symbol)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._symbol_reflection_offset_win, 3,5,1,3)
        self._symbol_reflection_ampl_range = Range(0, 1, 0.001, 0, 100)
        self._symbol_reflection_ampl_win = RangeWidget(self._symbol_reflection_ampl_range, self.set_symbol_reflection_ampl, "Distant Reflection Amplitude", "counter_slider", float)
        self.top_grid_layout.addWidget(self._symbol_reflection_ampl_win, 3,0,1,5)
        self._refl_delay_range = Range(0, 360, 1, 0, 100)
        self._refl_delay_win = RangeWidget(self._refl_delay_range, self.set_refl_delay, "Phase Offset (Degrees)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._refl_delay_win, 2,5,1,3)
        self._refl_amplitude_range = Range(0, 1, 0.001, 0, 100)
        self._refl_amplitude_win = RangeWidget(self._refl_amplitude_range, self.set_refl_amplitude, "Nearby Reflection Amplitude", "counter_slider", float)
        self.top_grid_layout.addWidget(self._refl_amplitude_win, 2,0,1,5)
        self._noise_level_range = Range(0, 160, 1, 0, 100)
        self._noise_level_win = RangeWidget(self._noise_level_range, self.set_noise_level, "Noise Level (dB)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_level_win, 4,0,1,8)
        self._direct_amplitude_range = Range(0, 1, 0.01, 1, 1000)
        self._direct_amplitude_win = RangeWidget(self._direct_amplitude_range, self.set_direct_amplitude, "Transmitted Signal Amplitude", "counter_slider", float)
        self.top_grid_layout.addWidget(self._direct_amplitude_win, 1,0,1,8)
        self.up_convert = blocks.multiply_vcc(1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=sps,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=sps,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Transmitted and Received Signals", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-3, 3)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ["Transmitted Signal", "Nearby Reflection", "Distant Reflection", "Noise", "Channel Total",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Transmitted and Received Signals", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-200, 0)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["Received Signal", "Transmitted Signal", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	512, #size
        	"Windowed Constellation", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.75, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ["Decoded Data", "Expected Data", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 2, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_const_sink_x_0_win)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(1, (rrc_taps))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.down_convert = blocks.multiply_vcc(1)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=constellation,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=True,
          log=False,
          )
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(constellation)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(constellation)
        self.carrier_source_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -carrier_frequency, 1, 0)
        self.carrier_source = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, carrier_frequency, 1, 0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vcc((symbol_reflection_ampl, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((refl_amplitude, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((direct_amplitude, ))
        self.blocks_delay_2_0 = blocks.delay(gr.sizeof_gr_complex*1, sps/4)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_gr_complex*1, sps/4)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, int(symbol_reflection_offset * sps))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(refl_delay/360.0 * samp_rate / carrier_frequency))
        self.blocks_copy_0 = blocks.copy(gr.sizeof_gr_complex*1)
        self.blocks_copy_0.set_enabled(True)
        self.blocks_complex_to_real_1_1_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='SER',
        	win_size=20000,
        	bits_per_symbol=bits_per_symbol,
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2**bits_per_symbol , 10000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.000001 * 10**(noise_level/20), 0)
        self.SER = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.SER.set_update_time(1.5)
        self.SER.set_title("")
        
        labels = ["SER", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.SER.set_min(i, 0)
            self.SER.set_max(i, 1)
            self.SER.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.SER.set_label(i, "Data {0}".format(i))
            else:
                self.SER.set_label(i, labels[i])
            self.SER.set_unit(i, units[i])
            self.SER.set_factor(i, factor[i])
        
        self.SER.enable_autoscale(False)
        self._SER_win = sip.wrapinstance(self.SER.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._SER_win, 0,7,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_complex_to_real_1_0_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.SER, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_real_1_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.down_convert, 1))    
        self.connect((self.blocks_complex_to_real_1, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_complex_to_real_1_0, 0), (self.qtgui_time_sink_x_1, 4))    
        self.connect((self.blocks_complex_to_real_1_0_0, 0), (self.qtgui_time_sink_x_1, 3))    
        self.connect((self.blocks_complex_to_real_1_1, 0), (self.qtgui_time_sink_x_1, 2))    
        self.connect((self.blocks_complex_to_real_1_1_0, 0), (self.qtgui_time_sink_x_1, 1))    
        self.connect((self.blocks_copy_0, 0), (self.blocks_delay_2, 0))    
        self.connect((self.blocks_copy_0, 0), (self.digital_constellation_decoder_cb_1, 0))    
        self.connect((self.blocks_copy_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))    
        self.connect((self.blocks_delay_2, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_delay_2_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_complex_to_real_1_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_complex_to_real_1_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.up_convert, 0))    
        self.connect((self.carrier_source, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.carrier_source_0, 0), (self.down_convert, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blks2_error_rate_0, 1))    
        self.connect((self.digital_constellation_modulator_0, 0), (self.fir_filter_xxx_0_0, 0))    
        self.connect((self.down_convert, 0), (self.blocks_delay_2_0, 0))    
        self.connect((self.down_convert, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.down_convert, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_copy_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.up_convert, 1))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_const_sink_x_0, 1))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.up_convert, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1, self.excess_bw, 45))
        self.blocks_delay_0_0.set_dly(int(self.symbol_reflection_offset * self.sps))
        self.blocks_delay_2.set_dly(self.sps/4)
        self.blocks_delay_2_0.set_dly(self.sps/4)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1, self.excess_bw, 45))

    def get_QAM(self):
        return self.QAM

    def set_QAM(self, QAM):
        self.QAM = QAM
        self.set_constellation(self.QAM)

    def get_symbol_reflection_offset(self):
        return self.symbol_reflection_offset

    def set_symbol_reflection_offset(self, symbol_reflection_offset):
        self.symbol_reflection_offset = symbol_reflection_offset
        self.blocks_delay_0_0.set_dly(int(self.symbol_reflection_offset * self.sps))

    def get_symbol_reflection_ampl(self):
        return self.symbol_reflection_ampl

    def set_symbol_reflection_ampl(self, symbol_reflection_ampl):
        self.symbol_reflection_ampl = symbol_reflection_ampl
        self.blocks_multiply_const_vxx_1_0.set_k((self.symbol_reflection_ampl, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_delay_0.set_dly(int(self.refl_delay/360.0 * self.samp_rate / self.carrier_frequency))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.carrier_source.set_sampling_freq(self.samp_rate)
        self.carrier_source_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.fir_filter_xxx_0_0.set_taps((self.rrc_taps))

    def get_refl_delay(self):
        return self.refl_delay

    def set_refl_delay(self, refl_delay):
        self.refl_delay = refl_delay
        self.blocks_delay_0.set_dly(int(self.refl_delay/360.0 * self.samp_rate / self.carrier_frequency))

    def get_refl_amplitude(self):
        return self.refl_amplitude

    def set_refl_amplitude(self, refl_amplitude):
        self.refl_amplitude = refl_amplitude
        self.blocks_multiply_const_vxx_1.set_k((self.refl_amplitude, ))

    def get_noise_level(self):
        return self.noise_level

    def set_noise_level(self, noise_level):
        self.noise_level = noise_level
        self.analog_noise_source_x_0.set_amplitude(0.000001 * 10**(self.noise_level/20))

    def get_max_phase_offset_ratio(self):
        return self.max_phase_offset_ratio

    def set_max_phase_offset_ratio(self, max_phase_offset_ratio):
        self.max_phase_offset_ratio = max_phase_offset_ratio

    def get_direct_amplitude(self):
        return self.direct_amplitude

    def set_direct_amplitude(self, direct_amplitude):
        self.direct_amplitude = direct_amplitude
        self.blocks_multiply_const_vxx_0.set_k((self.direct_amplitude, ))

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation

    def get_carrier_frequency(self):
        return self.carrier_frequency

    def set_carrier_frequency(self, carrier_frequency):
        self.carrier_frequency = carrier_frequency
        self.blocks_delay_0.set_dly(int(self.refl_delay/360.0 * self.samp_rate / self.carrier_frequency))
        self.carrier_source.set_frequency(self.carrier_frequency)
        self.carrier_source_0.set_frequency(-self.carrier_frequency)

    def get_bits_per_symbol(self):
        return self.bits_per_symbol

    def set_bits_per_symbol(self, bits_per_symbol):
        self.bits_per_symbol = bits_per_symbol

    def get_PSK(self):
        return self.PSK

    def set_PSK(self, PSK):
        self.PSK = PSK


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
