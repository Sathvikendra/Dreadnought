import cv2

# Input video file
input_file = 'input_video.mp4'

# Output video file
output_file = 'output_video.mp4'

# Open the input video file
cap = cv2.VideoCapture(input_file)

# Get the frames per second (fps) of the input video
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

# Loop through the frames of the input video
while cap.isOpened():
    # Read a frame from the input video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Skip 75% of the frames
    if cap.get(cv2.CAP_PROP_POS_FRAMES) % 4 != 0:
        continue

    # Write the frame to the output video
    out.write(frame)

    # Display the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()
