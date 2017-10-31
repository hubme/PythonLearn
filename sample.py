import pickle
f = open(r"E:\Python\PythonLearn\test\output_file.txt", "w");
pickle.dump(100, f)
pickle.dump(123.38, f)
pickle.dump((1, 3, "abc")), f)
pickle.dump([4, 5, 6], f)
f.close()