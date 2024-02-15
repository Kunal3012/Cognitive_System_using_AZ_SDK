from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import tkinter as tk
from PIL import ImageTk
class ImageAnalyzer:
    def __init__(self, cog_service_endpoint, cog_service_key):
        self.cog_service_endpoint = cog_service_endpoint
        self.cog_service_key = cog_service_key
        self.cv_client = self._initialize_client()

    def _initialize_client(self):
        credential = CognitiveServicesCredentials(self.cog_service_key)
        return ComputerVisionClient(self.cog_service_endpoint, credential)

    def analyze_image(self, image_file):
        print('Analyzing', image_file)

        # Specify features to be retrieved
        features = [
            VisualFeatureTypes.description,
            VisualFeatureTypes.tags,
            VisualFeatureTypes.categories,
            VisualFeatureTypes.brands,
            VisualFeatureTypes.objects,
            VisualFeatureTypes.adult
        ]

        # Get image analysis
        with open(image_file, mode="rb") as image_data:
            analysis = self.cv_client.analyze_image_in_stream(image_data, features)

        self._print_image_description(analysis.description)
        self._print_image_tags(analysis.tags)
        self._print_image_categories(analysis.categories)
        self._print_image_brands(analysis.brands)
        self._print_moderation_ratings(analysis.adult)
        self._print_image_objects(image_file, analysis.objects)

    def _print_image_description(self, description):
        print("Description: '{}' (confidence: {:.2f}%)".format(description.captions[0].text, description.captions[0].confidence * 100))

    def _print_image_tags(self, tags):
        if len(tags) > 0:
            print("Tags:")
            for tag in tags:
                print(" -'{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))

    def _print_image_categories(self, categories):
        if len(categories) > 0:
            print("Categories:")
            landmarks = []
            for category in categories:
                print(" -'{}' (confidence: {:.2f}%)".format(category.name, category.score * 100))
                if category.detail and category.detail.landmarks:
                    landmarks.extend(category.detail.landmarks)

            if landmarks:
                print("Landmarks:")
                for landmark in landmarks:
                    print(" -'{}' (confidence: {:.2f}%)".format(landmark.name, landmark.confidence * 100))

    def _print_image_brands(self, brands):
        if len(brands) > 0:
            print("Brands:")
            for brand in brands:
                print(" -'{}' (confidence: {:.2f}%)".format(brand.name, brand.confidence * 100))

    def _print_image_objects(self, image_file, objects):
        if len(objects) > 0:
            print("Objects in image:")

            # Prepare image for drawing
            fig = plt.figure(figsize=(8, 8))
            plt.axis('off')
            image = Image.open(image_file)
            draw = ImageDraw.Draw(image)
            color = 'cyan'

            for detected_object in objects:
                print(" -{} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))

                # Draw object bounding box
                r = detected_object.rectangle
                bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
                draw.rectangle(bounding_box, outline=color, width=3)
                plt.annotate(detected_object.object_property, (r.x, r.y), backgroundcolor=color)

            # Save annotated image
            plt.imshow(image)
            outputfile = 'objects.jpg'
            fig.savefig(outputfile)
            print('  Results saved in', outputfile)

    def _print_moderation_ratings(self, adult):
        ratings = 'Ratings:\n -Adult: {}\n -Racy: {}\n -Gore: {}'.format(adult.is_adult_content,
                                                                         adult.is_racy_content,
                                                                         adult.is_gory_content)
        print(ratings)
    def _print_image_objects(self, image_file, objects):
        if len(objects) > 0:
            print("Objects in image:")

            # Create a new pop-up window
            popup_window = tk.Tk()
            popup_window.title("Annotated Image")

            # Prepare image for drawing
            image = Image.open(image_file)
            draw = ImageDraw.Draw(image)
            color = 'cyan'

            for detected_object in objects:
                print(" -{} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))

                # Draw object bounding box
                r = detected_object.rectangle
                bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
                draw.rectangle(bounding_box, outline=color, width=3)

            # Convert the PIL Image to a PhotoImage for tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Display annotated image in the pop-up window
            label = tk.Label(popup_window, image=tk_image)
            label.image = tk_image
            label.pack()

            # Start the tkinter event loop
            popup_window.mainloop()