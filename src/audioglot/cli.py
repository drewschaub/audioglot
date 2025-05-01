"""
Command-line interface for Audioglot.
"""
import argparse
import sys

def main():
    """
    Main entry point for the Audioglot CLI.
    """
    parser = argparse.ArgumentParser(description="Audioglot - Transcribe and translate personal media.")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Transcribe command
    transcribe_parser = subparsers.add_parser("transcribe", help="Transcribe audio or video files")
    transcribe_parser.add_argument("input", help="Input file path (audio or video)")
    transcribe_parser.add_argument("--engine", choices=["faster-whisper", "whisper-cpp"], default="faster-whisper",
                                  help="Transcription engine to use")
    transcribe_parser.add_argument("--model", default="base", 
                                  help="Model to use for transcription")
    transcribe_parser.add_argument("--output", help="Output file path")
    
    # Translate command
    translate_parser = subparsers.add_parser("translate", help="Translate text")
    translate_parser.add_argument("input", help="Input file path with text to translate")
    translate_parser.add_argument("--service", choices=["deepl", "google-translate"], default="google-translate",
                                help="Translation service to use")
    translate_parser.add_argument("--language", required=True, help="Target language code (e.g., 'DE', 'FR')")
    translate_parser.add_argument("--output", help="Output file path")
    
    # Dataset command
    dataset_parser = subparsers.add_parser("dataset", help="Create a dataset for fine-tuning")
    dataset_parser.add_argument("input_dir", help="Directory with audio files")
    dataset_parser.add_argument("--transcript-dir", help="Directory with transcript files")
    dataset_parser.add_argument("--output-dir", required=True, help="Output directory for the dataset")
    dataset_parser.add_argument("--test-split", type=float, default=0.2, 
                               help="Proportion of data to use for testing")
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return 1
        
    if args.command == "transcribe":
        print(f"Transcribing {args.input} using {args.engine} with model {args.model}")
        # Will implement actual transcription code here
    
    elif args.command == "translate":
        print(f"Translating {args.input} to {args.language} using {args.service}")
        # Will implement actual translation code here
    
    elif args.command == "dataset":
        print(f"Creating dataset from {args.input_dir} to {args.output_dir}")
        # Will implement actual dataset creation code here
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 