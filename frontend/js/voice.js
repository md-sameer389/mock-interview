/**
 * Mock Interview Platform - Voice Interaction Module
 * Handles Text-to-Speech (TTS) and Speech-to-Text (STT)
 * Uses browser native Web Speech API - No External APIs!
 */

class VoiceManager {
    constructor() {
        this.synth = window.speechSynthesis;
        this.recognition = null;
        this.isSpeaking = false;
        this.isListening = false;
        this.voiceEnabled = true;
        this.currentUtterance = null;


        // Configuration
        this.speechRate = 1.0;
        this.speechPitch = 1.0;
        this.preferredVoice = null;



        // Initialize
        this.initSpeechRecognition();
        this.loadVoices();

        // Bind methods
        this.speak = this.speak.bind(this);
        this.stopSpeaking = this.stopSpeaking.bind(this);
        this.toggleListening = this.toggleListening.bind(this);
    }

    // ==================== TEXT TO SPEECH (INTERVIEWER) ====================

    loadVoices() {
        // Voices are loaded asynchronously
        let voices = this.synth.getVoices();
        if (voices.length > 0) {
            this.selectBestVoice(voices);
        } else {
            this.synth.onvoiceschanged = () => {
                voices = this.synth.getVoices();
                this.selectBestVoice(voices);
            };
        }
    }

    selectBestVoice(voices) {
        // Prioritize: 1. Google US English, 2. Microsoft David/Zira, 3. Any English
        // We want a professional sounding voice
        const preferred = voices.find(v => v.name.includes('Google US English')) ||
            voices.find(v => v.name.includes('Microsoft Zira')) ||
            voices.find(v => v.name.includes('Microsoft David')) ||
            voices.find(v => v.lang.startsWith('en'));

        if (preferred) {
            this.preferredVoice = preferred;
            console.log('Selected Voice:', preferred.name);
        }
    }

    speak(text, onEndCallback = null) {
        if (!this.voiceEnabled || !text) return;

        // Stop MIC if it's running (Prevent Echo)
        if (this.isListening) {
            this.stopListening();
        }

        // Stop any current speech
        this.stopSpeaking();

        // Create utterance
        const utterance = new SpeechSynthesisUtterance(text);
        if (this.preferredVoice) {
            utterance.voice = this.preferredVoice;
        }
        // Randomize pitch/rate slightly for variety
        utterance.rate = this.speechRate * (0.95 + Math.random() * 0.1);
        utterance.pitch = this.speechPitch * (0.95 + Math.random() * 0.1);



        // Events
        utterance.onstart = () => {
            this.isSpeaking = true;
            this.updateVisualizer(true);
            const statusEl = document.getElementById('interviewer-status');
            if (statusEl) {
                statusEl.textContent = 'Speaking...';
                statusEl.classList.add('active');
            }
        };

        utterance.onend = () => {
            this.isSpeaking = false;
            this.updateVisualizer(false);
            const statusEl = document.getElementById('interviewer-status');
            if (statusEl) {
                statusEl.textContent = 'Listening...';
                statusEl.classList.remove('active');
            }
            if (onEndCallback) onEndCallback();
        };

        utterance.onerror = (e) => {
            console.error('TTS Error:', e);
            this.isSpeaking = false;
            this.updateVisualizer(false);
        };

        this.currentUtterance = utterance;

        // Slight delay for realism (fixed)
        setTimeout(() => {
            this.synth.speak(utterance);
        }, 500);
    }

    stopSpeaking() {
        if (this.synth.speaking) {
            this.synth.cancel();
        }
        this.isSpeaking = false;
        this.updateVisualizer(false);
    }

    updateVisualizer(active) {
        const visualizer = document.getElementById('visualizer-circle');
        if (visualizer) {
            if (active) {
                visualizer.classList.add('active');
                visualizer.style.boxShadow = "0 0 60px rgba(108, 93, 211, 0.8)";
            } else {
                visualizer.classList.remove('active');
                visualizer.style.boxShadow = "0 0 40px rgba(108, 93, 211, 0.4)";
            }
        }
    }

    // ==================== SPEECH TO TEXT (CANDIDATE) ====================

    initSpeechRecognition() {
        // Check browser support
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (!SpeechRecognition) {
            console.warn('Speech Recognition not supported in this browser');
            // Hide mic button if not supported
            const micBtn = document.getElementById('mic-btn');
            if (micBtn) micBtn.style.display = 'none';
            return;
        }

        this.recognition = new SpeechRecognition();
        this.recognition.lang = 'en-US';
        this.recognition.continuous = true;
        this.recognition.interimResults = true;

        // Events
        this.recognition.onstart = () => {
            this.isListening = true;
            this.updateMicButton(true);
        };

        this.recognition.onend = () => {
            this.isListening = false;
            this.updateMicButton(false);
        };

        this.recognition.onresult = (event) => {
            let interimTranscript = '';
            let finalTranscript = '';

            for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                    finalTranscript += event.results[i][0].transcript;
                } else {
                    interimTranscript += event.results[i][0].transcript;
                }
            }

            // Update textarea
            const textarea = document.getElementById('answer-input');
            if (textarea && (finalTranscript || interimTranscript)) {
                if (finalTranscript) {
                    const currentVal = textarea.value;
                    const separator = currentVal.length > 0 && !currentVal.endsWith(' ') ? ' ' : '';
                    textarea.value = currentVal + separator + finalTranscript;
                    // Trigger input event for character counter update
                    textarea.dispatchEvent(new Event('input'));
                }
            }
        };

        this.recognition.onerror = (event) => {
            console.error('STT Error:', event.error);
            this.isListening = false;
            this.updateMicButton(false);

            if (event.error === 'not-allowed') {
                showMessage('Microphone access denied. Please enable permission.', 'error');
            }
        };
    }

    stopListening() {
        if (this.isListening && this.recognition) {
            this.recognition.stop();
            this.isListening = false;
            this.updateMicButton(false);
        }
    }

    toggleListening() {
        if (!this.recognition) {
            showMessage('Voice input not supported in this browser', 'error');
            return;
        }

        if (this.isListening) {
            this.stopListening();
        } else {
            // Stop interviewer if speaking
            this.stopSpeaking();
            try {
                this.recognition.start();
            } catch (e) {
                console.error('Recognition start error:', e);
            }
        }
    }

    updateMicButton(active) {
        const btn = document.getElementById('mic-btn');
        if (btn) {
            if (active) {
                btn.classList.add('listening');
                // Visualizer starts automatically via start/stop hooks
            } else {
                btn.classList.remove('listening');
            }
        }
    }
}

// ==================== AUDIO VISUALIZER (WEB AUDIO API) ====================
class AudioVisualizer {
    constructor() {
        this.audioContext = null;
        this.analyser = null;
        this.dataArray = null;
        this.source = null;
        this.animationId = null;
        this.isInitialized = false;
    }

    async init() {
        if (this.isInitialized) return;

        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.analyser = this.audioContext.createAnalyser();
            this.analyser.fftSize = 256; // Tradeoff between resolution and speed
            const bufferLength = this.analyser.frequencyBinCount;
            this.dataArray = new Uint8Array(bufferLength);
            this.isInitialized = true;
        } catch (e) {
            console.error("Web Audio API not supported", e);
        }
    }

    async connectMicrophone() {
        if (!this.isInitialized) await this.init();
        if (!this.audioContext) return;

        try {
            // Ensure context is running (browser policy)
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
            }

            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            this.source = this.audioContext.createMediaStreamSource(stream);
            this.source.connect(this.analyser);
            this.startVisualizing();
        } catch (e) {
            console.error("Microphone access denied for visualizer", e);
        }
    }

    disconnect() {
        if (this.source) {
            this.source.disconnect();
            this.source = null;
        }
        this.stopVisualizing();
    }

    startVisualizing() {
        const visualizerCircle = document.getElementById('visualizer-circle');

        let logCounter = 0; // consistent logging

        const draw = () => {
            if (!this.analyser) return; // safety

            this.animationId = requestAnimationFrame(draw);
            this.analyser.getByteFrequencyData(this.dataArray);

            // Calculate average volume (focus on lower frequencies for voice)
            let sum = 0;
            // Voice range is roughly lower half of FFT bins
            const voiceBins = Math.floor(this.dataArray.length / 2);
            for (let i = 0; i < voiceBins; i++) {
                sum += this.dataArray[i];
            }
            const average = sum / voiceBins;

            // Debug every 60 frames (~1 sec)
            logCounter++;
            if (logCounter % 60 === 0 && average > 0) {
                console.log("Visualizer Input Level:", average);
            }

            // Map 0-255 to scale 1.0-1.8
            // Add baseline volume gate to avoid noise jitter
            const volume = average > 5 ? average : 0; // Lowered gate to 5
            const scale = 1 + (volume / 255) * 1.5;

            // Update CSS variable
            if (visualizerCircle) {
                visualizerCircle.style.setProperty('--audio-level', scale);
                // Also tweak opacity/glow based on volume
                visualizerCircle.style.setProperty('--audio-glow', volume / 100);
            }
        };

        draw();
    }

    stopVisualizing() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
        // Reset styles
        const visualizerCircle = document.getElementById('visualizer-circle');
        if (visualizerCircle) {
            visualizerCircle.style.setProperty('--audio-level', 1);
            visualizerCircle.style.setProperty('--audio-glow', 0);
        }
    }

    startSimulation() {
        const visualizerCircle = document.getElementById('visualizer-circle');

        let time = 0;

        const simulate = () => {
            this.animationId = requestAnimationFrame(simulate);
            time += 0.1;

            // Create a ripple effect using sine waves with different phases
            const baseScale = 1.0;
            const noise = Math.random() * 0.1;

            const scale1 = baseScale + Math.sin(time) * 0.2 + noise;
            const scale2 = baseScale + Math.sin(time - 1) * 0.25 + noise;
            const scale3 = baseScale + Math.sin(time - 2) * 0.3 + noise;

            if (visualizerCircle) {
                // We update custom properties for each wave
                visualizerCircle.style.setProperty('--wave-1-scale', scale1);
                visualizerCircle.style.setProperty('--wave-2-scale', scale2);
                visualizerCircle.style.setProperty('--wave-3-scale', scale3);

                visualizerCircle.style.setProperty('--audio-glow', 0.5 + Math.sin(time) * 0.2);
            }
        };
        simulate();
    }

    stopSimulation() {
        this.stopVisualizing();
    }
}

// Enhance VoiceManager with Visualizer
const originalToggleListening = VoiceManager.prototype.toggleListening;
const originalStopListening = VoiceManager.prototype.stopListening;
const originalSpeak = VoiceManager.prototype.speak;

const visualizer = new AudioVisualizer();

VoiceManager.prototype.toggleListening = async function () {
    originalToggleListening.call(this); // Call original logic

    if (this.isListening) {
        // Just started listening
        await visualizer.connectMicrophone();
        document.getElementById('visualizer-circle').classList.add('mic-active');
    } else {
        // Just stopped
        visualizer.disconnect();
        document.getElementById('visualizer-circle').classList.remove('mic-active');
    }
};

VoiceManager.prototype.stopListening = function () {
    originalStopListening.call(this);
    visualizer.disconnect();
    const vC = document.getElementById('visualizer-circle');
    if (vC) vC.classList.remove('mic-active');
};

VoiceManager.prototype.speak = function (text, onEnd) {
    visualizer.startSimulation();
    document.getElementById('visualizer-circle').classList.add('ai-active');

    const wrappedOnEnd = () => {
        visualizer.stopSimulation();
        document.getElementById('visualizer-circle').classList.remove('ai-active');
        if (onEnd) onEnd();
    };

    originalSpeak.call(this, text, wrappedOnEnd);
};

// Export singleton instance
const voiceManager = new VoiceManager();
window.voiceManager = voiceManager;
