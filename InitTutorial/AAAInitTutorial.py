# File: T (Python 2.2)

import Live

class AAAInitTutorial:
    ''' A simple script to enable control over Live with the AAAInitTutorial controller '''
    
    def __init__(self, c_instance):
        self._cicle = 0
        Live.Base.log("LOG: AAAInitTutorial __init__")
    
    def application(self):
        Live.Base.log("LOG: AAAInitTutorial application")

    
    def song(self):
        Live.Base.log("LOG: AAAInitTutorial song")

    
    def disconnect(self):
        #Live -> Script 
        #Called right before we get disconnected from Live.
        Live.Base.log("LOG: AAAInitTutorial disconnect")
        

    
    def suggest_input_port(self):
        #Live -> Script
        #Live can ask the script for an input port name to find a suitable one.
        Live.Base.log("LOG: AAAInitTutorial suggest_input_port")

    
    def suggest_output_port(self):
        #Live -> Script
        #Live can ask the script for an output port name to find a suitable one.
        Live.Base.log("LOG: AAAInitTutorial suggest_output_port")

    
    def can_lock_to_devices(self):
        Live.Base.log("LOG: AAAInitTutorial can_lock_to_devices")
        return True

    
    def connect_script_instances(self, instanciated_scripts):
        #Called by the Application as soon as all scripts are initialized.
        #You can connect yourself to other running scripts here, as we do it
        #connect the extension modules (MackieControlXTs).
        Live.Base.log("LOG: AAAInitTutorial connect_script_instances")
        pass

    
    def request_rebuild_midi_map(self):
        #Script -> Live
        #When the internal MIDI controller has changed in a way that you need to rebuild
        #the MIDI mappings, request a rebuild by calling this function
        #This is processed as a request, to be sure that its not too often called, because
        #its time-critical.
        Live.Base.log("LOG: AAAInitTutorial request_rebuild_midi_map")

    
    def send_midi(self, midi_event_bytes):
        #Script -> Live
        #Use this function to send MIDI events through Live to the _real_ MIDI devices
        #that this script is assigned to.
        Live.Base.log("LOG: AAAInitTutorial send_midi")


    
    def refresh_state(self):
        #Live -> Script
        #Send out MIDI to completely update the attached MIDI controller.
        #Will be called when requested by the user, after for example having reconnected 
        #the MIDI cables...
        Live.Base.log("LOG: AAAInitTutorial refresh_state")
        
    def build_midi_map(self, midi_map_handle):
        #Live -> Script
        #Build DeviceParameter Mappings, that are processed in Audio time, or
        #forward MIDI messages explicitly to our receive_midi_functions.
        #Which means that when you are not forwarding MIDI, nor mapping parameters, you will 
        #never get any MIDI messages at all.
        Live.Base.log("LOG: AAAInitTutorial build_midi_map")
        feedback_rule = Live.MidiMap.CCFeedbackRule()
        feedback_rule.channel = 0
        feedback_rule.cc_no = 16
        feedback_rule.cc_value_map = tuple()
        feedback_rule.delay_in_ms = -1.0
        Live.MidiMap.map_midi_cc_with_feedback_map(midi_map_handle, self.song().master_track.mixer_device.volume, 0, 0, Live.MidiMap.MapMode.absolute_14_bit, feedback_rule)
        
        for channel in range(4):
            MidiMap.forward_midi_cc(script_handle, midi_map_handle, channel, AXIOM_BUT9)
            for slider in range(8):
                track_index = slider + channel * 8
                if len(self._SliderSection__parent.song().tracks) > track_index:
                    feedback_rule.channel = 0
                    feedback_rule.cc_no = AXIOM_SLIDERS[slider]
                    feedback_rule.cc_value_map = tuple()
                    feedback_rule.delay_in_ms = -1.0
                    MidiMap.map_midi_cc_with_feedback_map(midi_map_handle, self._SliderSection__parent.song().tracks[track_index].mixer_device.volume, channel, AXIOM_SLIDERS[slider], MidiMap.MapMode.absolute_14_bit, feedback_rule)
                    MidiMap.forward_midi_cc(script_handle, midi_map_handle, channel, AXIOM_BUTTONS[slider])
                else:
                    break
            
        

    
    def update_display(self):
        # Live -> Script
        # Aka on_timer. Called every 100 ms and should be used to update display relevant
        if(self._cicle > 100):
            self._cicle = 0
            Live.Base.log("LOG: AAAInitTutorial update_display (100 calls)")
        else:
            self._cicle = self._cicle+1
        

    
    def receive_midi(self, midi_bytes):
        # Live -> Script
        # MIDI messages are only received through this function, when explicitly 
        # forwarded in 'build_midi_map'.
        Live.Base.log("LOG: AAAInitTutorial receive_midi")
        
   
    def lock_to_device(self, device):
        #Live -> Script
        #Live can tell the script to lock to a given device
        Live.Base.log("LOG: AAAInitTutorial lock_to_device")

    
    def unlock_from_device(self, device):
        #Live -> Script
        #Live can tell the script to unlock from a given device
        Live.Base.log("LOG: AAAInitTutorial unlock_from_device")

    
    def set_appointed_device(self, device):
        #Live -> Script
        #Live can tell the script which device to use if it is not locked
        #This is a substitute mechanism for the listeners used by older scripts
        Live.Base.log("LOG: AAAInitTutorial set_appointed_device")

    
    def toggle_lock(self):
        #Script -> Live
        #Use this function to toggle the script's lock on devices
        Live.Base.log("LOG: AAAInitTutorial toggle_lock")

    
    def suggest_map_mode(self, cc_no):
        #Live -> Script
        #Live can ask the script to suggest a map mode for the given CC
        Live.Base.log("LOG: AAAInitTutorial suggest_map_mode")
    
    def restore_bank(self, bank):
        Live.Base.log("LOG: AAAInitTutorial restore_bank")        
