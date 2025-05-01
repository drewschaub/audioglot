"""
Factory for creating translator instances.
"""

def create_translator(service, **kwargs):
    """
    Create a translator instance based on the specified service.
    
    Args:
        service (str): The translation service to use ('deepl' or 'google-translate').
        **kwargs: Additional arguments to pass to the translator constructor.
        
    Returns:
        A translator instance that can translate text.
        
    Raises:
        ValueError: If the specified service is not supported.
    """
    if service == "deepl":
        from .deepl import DeepLTranslator
        return DeepLTranslator(**kwargs)
    elif service == "google-translate":
        from .google_translate import GoogleTranslator
        return GoogleTranslator(**kwargs)
    else:
        raise ValueError(f"Unsupported translation service: {service}") 