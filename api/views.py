from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn import svm
import numpy as np


class SVMClassifierView(APIView):
    def post(self, request):
        try:
            training_data = request.data.get("trainingData", [])
            class_name = request.data.get("className", [])
            input_feature = request.data.get("inputFeature", [])

            # Validasi input
            if not training_data or not class_name or not input_feature:
                return Response(
                    {"error": "trainingData, className, dan inputFeature wajib diisi."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Konversi ke numpy array
            X = np.array(training_data)
            y = np.array(class_name)
            input_data = np.array([input_feature])

            # Buat model SVM dan latih
            model = svm.SVC(kernel="linear")  # bisa ganti 'rbf' atau lainnya
            model.fit(X, y)

            # Prediksi input
            prediction = model.predict(input_data)

            return Response({"status": "success", "result": prediction[0]})

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
