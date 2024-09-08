def encode_know_faces(
    model: str = 'hog', encodings_location: Path = DEFAULT_ENCODINGS_PATH
) -> None:
    names = []
    encodings = []
    
    for filepath in Path("training").glob("*/*"):
        name = filepath.parts[-2]
        image = face_recognition.load_image_file(filepath)
        
        face_locations = face_recognition.face_locations(image, model= model)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)
            
    with open(encodings_location, "wb") as f:
        pickle.dump((names, encodings), f)
        names.append(name)
    return None

