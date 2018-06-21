
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;

import java.util.Properties;


public class SliderVerCode {
	
	private String url = "https://id.163yun.com/login?referrer=https://dun.163.com/dashboard&h=yd&fromyd=baiduP2_YZM_CP1934";
	private String xpathBG = "//*[@id=\"bg\"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[1]";
	private String xpathSlider = "//*[@id=\"bg\"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[2]";
	
	private int move_distance = 0;
	
	private String info[];
	
	

	/***
	 * 
	 * @param url: the URL of verification code need to be recognized 
	 * @param xpathBG: the xpath of background image (can find by Chrome browser developer function)
	 * @param xpathSlider: the xpath of Slider image
	 */
	public SliderVerCode(String url, String xpathBG, String xpathSlider){
		if (url != null) 
			this.url = url;
		if (xpathBG != null)
			this.xpathBG = xpathBG;
		if (xpathSlider != null)
			this.xpathSlider = xpathSlider;
		
		info = new String[8];
		this.FindSlidePos();
	}
	
	private void FindSlidePos() {
		
		Process p = null;
		
		try {
			
			// python installed path (need install module: OpenCV/cv2, selenium
			String python_path = "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/bin/python3.6";
			
			// python file path
			String python_file_path = "/Users/yiqian/Documents/GitHub/SliderVer/JavaAPI/src/PythonFile/MoveSlider.py";
			
			String[] args = new String[] {python_path, python_file_path, this.url, this.xpathBG, this.xpathSlider};

			p = Runtime.getRuntime().exec(args);
			String s;
			
			int count = 0;
			
			BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(p.getInputStream()));
			while ((s = bufferedReader.readLine()) != null) {
				System.out.println(s);
				this.info[count] = s;
				count ++;
			}
			p.waitFor();
		
			System.out.println(p.waitFor());
		}catch(Exception e) {
			
			e.printStackTrace();
		}finally {
			p.destroy();
		}
		
	}
	
	
	/***
	 * 
	 * @return slider move distance
	 */
	public int getMove_distance() {
		return Integer.parseInt(this.info[7]);
	}
	
	public static void main(String[] args){
		
		
		SliderVerCode find = new SliderVerCode(null, null, null);
		
		String result = "the move distance is: " + String.valueOf(find.getMove_distance());
		System.out.println(result);
	}
}

/***
 --- 
 embedding python in JAVA by jython 
 but some python module only implement by C language (CPython) not JAVA
 so there are lots of limitations in jython methods
 ---

import org.python.core.Py;
import org.python.core.PyFunction;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.core.PySystemState;

import org.python.util.PythonInterpreter;
import java.util.Properties;

public class SlideVerCode {
	
	public static void main(String args[]) {
		
		Properties props = new Properties();
		props.put("python.console.encoding", "UTF-8");
		props.put("python.security.respectJavaAccessibility", "false");
		props.put("python.import.site", "false");
		
		Properties preprops = System.getProperties();
		
		PythonInterpreter.initialize(preprops, props, new String[0]);
		
		PythonInterpreter interpreter = new PythonInterpreter();
		
		PySystemState sys = Py.getSystemState();
		
		// Python files path
		sys.path.add("/Users/yiqian/Documents/GitHub/SliderVer/JavaAPI/src/PythonFile/");
		// cv2 module path
		//sys.path.add("/Users/yiqian/miniconda3/lib/python3.6/site-packages/");
		
		sys.path.add("/Users/yiqian/jython2.7.0/Lib");
		interpreter.exec("import sys");
		interpreter.exec("sys.path.append('')");
		interpreter.exec("import cv2");
		interpreter.exec("import importlib");
		interpreter.exec("import CalSliderSize");
		interpreter.exec("import FindSliderPos");
		interpreter.execfile("src/PythonFile/MoveSlider.py");
		
	}
}

***/




