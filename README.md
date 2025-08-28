# folder2txt

`folder2txt`는 사용자가 선택한 폴더 안의 파일 목록을 **텍스트 파일**로 저장해주는 간단한 유틸리티입니다.  
저장되는 텍스트 파일에는 각 파일의 **전체 경로**가 기록됩니다.

---

## 주요 기능
- Tkinter 기반 GUI 폴더 선택 창 제공
- 선택한 폴더 안의 모든 파일 이름을 읽어와 `폴더이름_file_list.txt` 형식으로 저장
- 텍스트 파일에는 파일 이름이 아닌 **절대 경로(full path)** 가 기록됨
- PyInstaller로 패키징 시 GUI 모드 실행(`-w` 옵션)으로 콘솔 창 없이 사용 가능

---

## 사용 방법

### 1. Python 스크립트로 실행
```bash
python folder2txt.py
```
실행하면 폴더 선택 창이 뜨며, 원하는 폴더를 선택하면 해당 폴더 안에  
`<폴더명>_file_list.txt` 파일이 생성됩니다.

예시:  
```
C:/Users/Desktop/test/
 ├─ a.txt
 ├─ b.csv
 └─ test_file_list.txt   ← 자동 생성
```

`test_file_list.txt` 내용:
```
C:/Users/Desktop/test/a.txt
C:/Users/Desktop/test/b.csv
```

## 설치 및 요구 사항
- Python 3.x
- Tkinter (Python 기본 포함)
- (선택) PyInstaller (`pip install pyinstaller`)

---

## 한계
- 현재는 선택한 폴더 **직접 하위 파일만** 저장합니다.  
  (재귀적으로 하위 폴더까지 포함하려면 `os.walk`로 확장 가능)
- 출력 파일은 항상 **선택한 폴더 내부**에 생성됩니다.

---


