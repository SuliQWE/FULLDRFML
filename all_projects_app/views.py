from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (StudentPerformanceSerializers, TitanicSerializers, HouseSerializers,
                          BankSerializers, DiabetesSerializers, AvocadoSerializers,
                          MushroomSerializers, TelecomSerializers,HRESerializer)
import joblib
import os
from django.conf import settings
import numpy as np

student_scaler = joblib.load('models/student_scaler.pkl')
student_model = joblib.load('models/student_model.pkl')
# student_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'student_scaler.pkl')
# student_scaler = joblib.load(student_scaler_path)

# student_model_path = os.path.join(settings.BASE_DIR, 'models', 'student_model.pkl')
# student_model = joblib.load(student_model_path)

titanic_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'scaler_titanic (1).pkl')
titanic_model_path = os.path.join(settings.BASE_DIR, 'models', 'log_model_titanic (1).pkl')

titanic_scaler = joblib.load(titanic_scaler_path)
titanic_model = joblib.load(titanic_model_path)

house_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'house_scaler.pkl')
house_model_path = os.path.join(settings.BASE_DIR, 'models', 'house_model.pkl')

house_scaler = joblib.load(house_scaler_path)
house_model = joblib.load(house_model_path)

bank_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'scaler_bank.pkl')
bank_model_path = os.path.join(settings.BASE_DIR, 'models', 'log_model_bank.pkl')

bank_scaler = joblib.load(bank_scaler_path)
bank_model = joblib.load(bank_model_path)

diabetes_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'diabetes_scaler.pkl')
diabetes_model_path = os.path.join(settings.BASE_DIR, 'models', 'diabetes_log_model.pkl')

diabetes_scaler = joblib.load(diabetes_scaler_path)
diabetes_model = joblib.load(diabetes_model_path)

avocado_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'scaler_avocado.pkl')
avocado_model_path = os.path.join(settings.BASE_DIR, 'models', 'log_model_avocado.pkl')

avocado_scaler = joblib.load(avocado_scaler_path)
avocado_model = joblib.load(avocado_model_path)

mushroom_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'mushroom_scaler.pkl')
mushroom_model_path = os.path.join(settings.BASE_DIR, 'models', 'mushroom_random_model.pkl')

mushroom_scaler = joblib.load(mushroom_scaler_path)
mushroom_model = joblib.load(mushroom_model_path)

telecom_scaler_path = os.path.join(settings.BASE_DIR, 'models', 'logistic_scaler.pkl')
telecom_model_path = os.path.join(settings.BASE_DIR, 'models', 'logistic_model.pkl')

telecom_scaler = joblib.load(telecom_scaler_path)
telecom_model = joblib.load(telecom_model_path)

hre_model = joblib.load('models/hre_model.pkl')
hre_scaler = joblib.load('models/hre_scaler.pkl')




gender = ['male']
race_ethnicity = ['group B', 'group C', 'group D' , 'group E']
parental_level_of_education = ["bachelor's degree", 'high school', "master's degree", 'some college', 'some high school']
lunch = ['standard']
test_preparation_course = ['none']
Sex = ['female']
Embarked = ['Q', 'S']
Neighborhoods = ['Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards',
                 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes',
                 'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
                 'StoneBr', 'Timber', 'Veenker']
person_gender = ['male']
person_education = ['Bachelor', 'Doctorate', 'High School', 'Master']
person_home_ownership = ['OTHER', 'OWN', 'RENT']
loan_intent = ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE']
previous_loan_defaults_on_file = ['Yes']
color_category = ['dark green', 'green', 'purple']
cap_shapes = ['c', 'f', 'k', 's', 'x']
cap_surfaces = ['g', 's', 'y']
cap_color = ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']
odor = ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y']
gill_color = ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']
stalk_root = ['c', 'e', 'r']
stalk_surface_above_ring = ['k', 's', 'y']
stalk_surface_below_ring = ['k', 's', 'y']
stalk_color_above_ring = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
stalk_color_below_ring = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
veil_color = ['o', 'w', 'y']
ring_number = ['o', 't']
ring_type = ['f', 'l', 'n', 'p']
spore_print_color = ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
population = ['c', 'n', 's', 'v', 'y']
habitat = ['g', 'l', 'm', 'p', 'u', 'w']
telecom_gender = ['Male']
Partner = ['Yes']
Dependents = ['Yes']
PhoneService = ['Yes']
MultipleLines = ['No phone service', 'Yes']
InternetService = ['Fiber optic', 'No']
OnlineSecurity = ['No internet service', 'Yes']
OnlineBackup = ['No internet service', 'Yes']
DeviceProtection = ['No internet service', 'Yes']
TechSupport = ['No internet service', 'Yes']
StreamingTV = ['No internet service', 'Yes']
StreamingMovies = ['No internet service', 'Yes']
Contract = ['One year', 'Two year']
PaperlessBilling = ['Yes']
PaymentMethod = ['Credit card (automatic)', 'Electronic check', 'Mailed check']
Business = ['Travel_Frequently', 'Travel_Rarely']
Department = ['Research & Development', 'Sales']
Education = ['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree']
Gender_hre = ['Male']
job = ['Human Resources', 'Laboratory Technician', 'Manager',
           'Manufacturing Director', 'Research Director', 'Research Scientist',
           'Sales Executive', 'Sales Representative']
Status = ['Married', 'Single']
Overtime = ['Yes']


class StudentPredict(views.APIView):
 def post(self, request):
     serializer = StudentPerformanceSerializers(data=request.data)
     if serializer.is_valid():
         data = serializer.validated_data
         new_gender = data.get('gender')
         gender1or_0 = [1 if new_gender == i else 0 for i in gender]

         new_race = data.get('race_ethnicity')
         race1or_0 = [1 if new_race == i else 0 for i in race_ethnicity]

         new_parental = data.get('parental_level_of_education')
         parental1or_0 = [1 if new_parental == i else 0 for i in parental_level_of_education]

         new_lunch = data.get('lunch')
         lunch1or_0 = [1 if new_lunch == i else 0 for i in lunch]

         new_test = data.get('test_preparation_course')
         test1or_0 = [1 if new_test == i else 0 for i in test_preparation_course]

         features = [data['reading_score'], data['math_score']] + gender1or_0 + race1or_0 + parental1or_0 + lunch1or_0 + test1or_0
         scaled_data = student_scaler.transform([features])
         pred = student_model.predict(scaled_data)[0]
         # student = serializer.save(student_predicted=round(pred))

         return Response({'Predict': round(pred)}, status.HTTP_200_OK)
     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class TitanicPredict(views.APIView):
    def post(self, request):
        serializer = TitanicSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_sex = data.get('Sex')
            sex1or_0 = [1 if new_sex == i else 0 for i in Sex]

            new_embarked = data.get('Embarked')
            embarked1or_0 = [1 if new_embarked == i else 0 for i in Embarked]

            features = [data['Pclass']] + sex1or_0 + [data['Age'], data['SibSp'],
                                                      data['Parch'], data['Fare'],
                                                      data['SibParch']] + embarked1or_0
            scaled_data = titanic_scaler.transform([features])
            pred = titanic_model.predict(scaled_data)[0]

            return Response({'Predict': int(pred)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class HousePredict(views.APIView):
    def post(self, request):
        serializer = HouseSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_neighborhood = data.get('Neighborhood')
            neighborhood1or_0 = [1 if new_neighborhood == i else 0 for i in Neighborhoods]

            features = [
                data['GrLivArea'],
                data['YearBuilt'],
                data['GarageCars'],
                data['TotalBsmtSF'],
                data['FullBath'],
                data['OverallQual'],
            ] + neighborhood1or_0
            scaled_data = house_scaler.transform([features])
            pred = house_model.predict(scaled_data)[0]
            #house = serializer.save(predicted_price=round(pred))

            return Response({'Predict Price': round(pred)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class BankPredict(views.APIView):
    def post(self, request):
        serializer = BankSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_gender = data.get('person_gender')
            gender1or_0 = [1 if new_gender == i else 0 for i in person_gender]

            new_education = data.get('person_education')
            education1or_0 = [1 if new_education == i else 0 for i in person_education]

            new_ownership = data.get('person_home_ownership')
            ownership1or_0 = [1 if new_ownership == i else 0 for i in person_home_ownership]

            new_intent = data.get('loan_intent')
            intent1or_0 = [1 if new_intent == i else 0 for i in loan_intent]

            new_defaults = data.get('previous_loan_defaults_on_file')
            defaults1or_0 = [1 if new_defaults == i else 0 for i in previous_loan_defaults_on_file]

            features = ([data['person_age'], data['person_income'], data['person_emp_exp'],
                        data['loan_amnt'], data['loan_int_rate'], data['loan_percent_income'],
                        data['cb_person_cred_hist_length'], data['credit_score']] + gender1or_0
                        + education1or_0 + ownership1or_0 + intent1or_0 + defaults1or_0)
            scaled_data = bank_scaler.transform([features])
            proba = bank_model.predict_proba(scaled_data)[0]
            probability = float(proba[1])
            if probability > 0.5:
                bank_label = 'Yes'
            else:
                bank_label = 'No'
            return Response({'Approved': bank_label , 'Probability': round(probability, 2)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class DiabetesPredict(views.APIView):
    def post(self, request):
        serializer = DiabetesSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = [data['Pregnancies'], data['Glucose'], data['BloodPressure'], data['SkinThickness'],
                        data['Insulin'], data['BMI'], data['DiabetesPedigreeFunction'], data['Age']]
            scaled_data = diabetes_scaler.transform([features])
            proba = diabetes_model.predict_proba(scaled_data)[0]
            probability = float(proba[1])
            if probability > 0.5:
                diabetes_label = 'Yes'
            else:
                diabetes_label = 'No'
            return Response({'Diabetes': diabetes_label, 'Probability': round(probability, 2)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class AvocadoPredict(views.APIView):
    def post(self, request):
        serializer = AvocadoSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_color_category = data.get('color_category')
            color_category1or_0 = [1 if new_color_category == i else 0 for i in color_category]

            features = [data['firmness'], data['hue'], data['saturation'],
                        data['brightness'], data['sound_db'], data['weight_g'],
                        data['size_cm3']] + color_category1or_0
            scaled_data = avocado_scaler.transform([features])
            proba = avocado_model.predict_proba(scaled_data)[0]
            ripeness_map = ['hard', 'pre-conditioned', 'breaking', 'firm-ripe', 'ripe']
            pred_index = np.argmax(proba)
            return Response({
                "ripeness": ripeness_map[pred_index],
                "probability": round(float(proba[pred_index]), 2)
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MushroomPredict(views.APIView):
    def post(self, request):
        serializer = MushroomSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_cap_shape = data.get('cap_shape')
            cap_shape1or_0 = [1 if new_cap_shape == i else 0 for i in cap_shapes]

            new_cap_surface = data.get('cap_surface')
            cap_surface1or_0 = [1 if new_cap_surface == i else 0 for i in cap_surfaces]

            new_cap_color = data.get('cap_color')
            cap_color1or_0 = [1 if new_cap_color == i else 0 for i in cap_color]

            new_bruises = data.get('bruises')
            bruises1or_0 = [1 if new_bruises == 't' else 0]

            new_odor = data.get('odor')
            odor1or_0 = [1 if new_odor == i else 0 for i in odor]

            new_gill_attachment = data.get('gill_attachment')
            gill_attachment1or_0 = [1 if new_gill_attachment == 'f' else 0]

            new_gill_spacing = data.get('gill_spacing')
            gill_spacing1or_0 = [1 if new_gill_spacing == 'w' else 0]

            new_gill_size = data.get('gill_size')
            gill_size1or_0 = [1 if new_gill_size == 'n' else 0]

            new_gill_color = data.get('gill_color')
            gill_color1or_0 = [1 if new_gill_color == i else 0 for i in gill_color]

            new_stalk_shape = data.get('stalk_shape')
            stalk_shape1or_0 = [1 if new_stalk_shape == 't' else 0]

            new_stalk_root = data.get('stalk_root')
            stalk_root1or_0 = [1 if new_stalk_root == i else 0 for i in stalk_root]

            new_stalk_surface_above_ring = data.get('stalk_surface_above_ring')
            stalk_surface_above_ring1or_0 = [1 if new_stalk_surface_above_ring == i else 0 for i in stalk_surface_above_ring]

            new_stalk_surface_below_ring = data.get('stalk_surface_below_ring')
            stalk_surface_below_ring1or_0 = [1 if new_stalk_surface_below_ring == i else 0 for i in stalk_surface_below_ring]

            new_stalk_color_above_ring = data.get('stalk_color_above_ring')
            stalk_color_above_ring1or_0 = [1 if new_stalk_color_above_ring == i else 0 for i in stalk_color_above_ring]

            new_stalk_color_below_ring = data.get('stalk_color_below_ring')
            stalk_color_below_ring1or_0 = [1 if new_stalk_color_below_ring == i else 0 for i in stalk_color_below_ring]

            new_veil_color = data.get('veil_color')
            veil_color1or_0 = [1 if new_veil_color == i else 0 for i in veil_color]

            new_ring_number = data.get('ring_number')
            ring_number1or_0 = [1 if new_ring_number == i else 0 for i in ring_number]

            new_ring_type = data.get('ring_type')
            ring_type1or_0 = [1 if new_ring_type == i else 0 for i in ring_type]

            new_spore_print_color = data.get('spore_print_color')
            spore_print_color1or_0 = [1 if new_spore_print_color == i else 0 for i in spore_print_color]

            new_population = data.get('population')
            population1or_0 = [1 if new_population == i else 0 for i in population]

            new_habitat = data.get('habitat')
            habitat1or_0 = [1 if new_habitat == i else 0 for i in habitat]

            features = ([] + cap_shape1or_0 + cap_surface1or_0 + cap_color1or_0 + bruises1or_0
                        + odor1or_0 + gill_attachment1or_0 + gill_spacing1or_0 + gill_size1or_0
                        + gill_color1or_0 + stalk_shape1or_0 + stalk_root1or_0 + stalk_surface_above_ring1or_0
                        + stalk_surface_below_ring1or_0 + stalk_color_above_ring1or_0 + stalk_color_below_ring1or_0
                        + veil_color1or_0 + ring_number1or_0 + ring_type1or_0 + spore_print_color1or_0
                        + population1or_0 + habitat1or_0)
            scaled_data = mushroom_scaler.transform([features])
            proba = mushroom_model.predict_proba(scaled_data)[0]
            probability = float(proba[1])
            if probability > 0.5:
                mushroom_label = 'Yes'
            else:
                mushroom_label = 'No'
            return Response({'Poisonous': mushroom_label, 'Probability': round(probability, 2)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class TelecomPredict(views.APIView):
    def post(self, request):
        serializer = TelecomSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_gender = data.get('gender')
            gender1or_0 = [1 if new_gender == i else 0 for i in gender]

            new_partner = data.get('Partner')
            partner1or_0 = [1 if new_partner == i else 0 for i in Partner]

            new_depends = data.get('Dependents')
            depends1or_0 = [1 if new_depends == i else 0 for i in Dependents]

            new_phone = data.get('PhoneService')
            phone1or_0 = [1 if new_phone == i else 0 for i in PhoneService]

            new_multiple = data.get('MultipleLines')
            multiple1or_0 = [1 if new_multiple == i else 0 for i in MultipleLines]

            new_internet = data.get('InternetService')
            internet1or_0 = [1 if new_internet == i else 0 for i in InternetService]

            new_security = data.get('OnlineSecurity')
            security1or_0 = [1 if new_security == i else 0 for i in OnlineSecurity]

            new_backup = data.get('OnlineBackup')
            backup1or_0 = [1 if new_backup == i else 0 for i in OnlineBackup]

            new_device = data.get('DeviceProtection')
            device1or_0 = [1 if new_device == i else 0 for i in DeviceProtection]

            new_support = data.get('TechSupport')
            support1or_0 = [1 if new_support == i else 0 for i in TechSupport]

            new_streaming = data.get('StreamingTV')
            streaming1or_0 = [1 if new_streaming == i else 0 for i in StreamingTV]

            new_movies = data.get('StreamingMovies')
            movies1or_0 = [1 if new_movies == i else 0 for i in StreamingMovies]

            new_contract = data.get('Contract')
            contract1or_0 = [1 if new_contract == i else 0 for i in Contract]

            new_paperless = data.get('PaperlessBilling')
            paperless1or_0 = [1 if new_paperless == i else 0 for i in PaperlessBilling]

            new_payment = data.get('PaymentMethod')
            payment1or_0 = [1 if new_payment == i else 0 for i in PaymentMethod]

            features = ([data['SeniorCitizen'], data['tenure'], data['MonthlyCharges'], data['TotalCharges']] + gender1or_0
                        + partner1or_0 + depends1or_0 + phone1or_0 + multiple1or_0 + internet1or_0 + security1or_0 + backup1or_0
                        + device1or_0 + support1or_0 + streaming1or_0 + movies1or_0 + contract1or_0 + paperless1or_0 + payment1or_0)
            scaled_data = telecom_scaler.transform([features])
            proba = telecom_model.predict_proba(scaled_data)[0]
            probability = float(proba[0])
            print(telecom_model.classes_, proba)
            if probability > 0.5:
                telecom_label = 'Yes'
            else:
                telecom_label = 'No'
            return Response({'Churn': telecom_label, 'Probability': round(probability, 2)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class HREPredict(APIView):
    def post(self, request):
        serializer = HRESerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            new_business = data.pop('BusinessTravel')
            business1or_0 = [1 if new_business == i else 0 for i in Business]
            new_department = data.pop('Department')
            department1or_0 = [1 if new_department == i else 0 for i in Department]
            new_education = data.pop('EducationField')
            education1or_0 = [1 if new_education == i else 0 for i in Education]
            new_gender = data.pop('Gender')
            gender1or_0 = [1 if new_gender == i else 0 for i in Gender_hre]
            new_job = data.pop('JobRole')
            job1or_0 = [1 if new_job == i else 0 for i in job]
            new_marital = data.pop('MaritalStatus')
            marital1or_0 = [1 if new_marital == i else 0 for i in Status]
            new_over = data.pop('OverTime')
            over1or_0 = [1 if new_over == i else 0 for i in Overtime]
            instance = [
                    data['Age'],
                    data['DailyRate'],
                    data['DistanceFromHome'],
                    data['Education'],
                    data['EnvironmentSatisfaction'],
                    data['HourlyRate'],
                    data['JobInvolvement'],
                    data['JobLevel'],
                    data['JobSatisfaction'],
                    data['MonthlyIncome'],
                    data['MonthlyRate'],
                    data['NumCompaniesWorked'],
                    data['PercentSalaryHike'],
                    data['PerformanceRating'],
                    data['RelationshipSatisfaction'],
                    data['StockOptionLevel'],
                    data['TotalWorkingYears'],
                    data['TrainingTimesLastYear'],
                    data['WorkLifeBalance'],
                    data['YearsAtCompany'],
                    data['YearsInCurrentRole'],
                    data['YearsSinceLastPromotion'],
                    data['YearsWithCurrManager']
                ] + business1or_0 + department1or_0 + education1or_0 + gender1or_0 + job1or_0 + marital1or_0 + over1or_0
            X = np.array(instance).reshape(1, -1)
            scaled_data = hre_scaler.transform(X)
            pred = hre_model.predict(scaled_data)[0]
            proba = hre_model.predict_proba(scaled_data)[0][1]
            if proba < 0.3:
                risk_level = 'Низкий'
                answer = 'Сотрудник останется в компании'
            elif proba < 0.7:
                risk_level = 'Средний'
                answer = 'Сотрудник возможно уйдет'
            else:
                risk_level = 'Высокий'
                answer = 'Сотрудник уйдет'
            hre_label = 'Yes' if proba > 0.5 else 'No'

            return  Response({'hre_label': hre_label,
                              'probability': round(float(proba),2),
                              'risk_level': risk_level,
                              'message': answer}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

