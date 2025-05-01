"""
Factory for creating transcriber instances.
"""

def create_transcriber(engine, **kwargs):
    """
    Create a transcriber instance based on the specified engine.
    
    Args:
        engine (str): The transcription engine to use ('faster-whisper' or 'whisper-cpp').
        **kwargs: Additional arguments to pass to the transcriber constructor.
        
    Returns:
        A transcriber instance that can transcribe audio files.
        
    Raises:
        ValueError: If the specified engine is not supported.
    """
    if engine == "faster-whisper":
        from .faster_whisper import FasterWhisperTranscriber
        return FasterWhisperTranscriber(**kwargs)
    elif engine == "whisper-cpp":
        from .whisper_cpp import WhisperCppTranscriber
        return WhisperCppTranscriber(**kwargs)
    else:
        raise ValueError(f"Unsupported transcription engine: {engine}") 