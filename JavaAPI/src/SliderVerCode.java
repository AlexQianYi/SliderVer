
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;

public class SliderVerCode {
	
	private String url = "https://id.163yun.com/login?referrer=https://dun.163.com/dashboard&h=yd&fromyd=baiduP2_YZM_CP1934";
	private String xpathBG = "//*[@id=\"bg\"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[1]";
	private String xpathSlider = "//*[@id=\"bg\"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[2]";
	
	private int move_distance = 0;
	
	

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
		
		this.FindSlidePos();
	}
	
	private void FindSlidePos() {
		
		Process p = null;
		
		try {
			String[] args = new String[] {"python", "/Users/yiqian/Documents/GitHub/SliderVer/JavaAPI/src/PythonFile/MoveSlider.py"};
			//String python_main_file = "python /Users/yiqian/Documents/GitHub/SliderVer/JavaAPI/src/PythonFile/MoveSlider.py";
			String info = "import urllib";
			System.out.println('a');
			p = Runtime.getRuntime().exec(info);
			String s;
			
			BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(p.getInputStream()));
			while ((s = bufferedReader.readLine()) != null) {
				System.out.println(s);
			}
			//p.waitFor();
			System.out.println('b');
			
			
			//InputStreamReader stdin = new InputStreamReader(p.getInputStream());
			//LineNumberReader input = new LineNumberReader(stdin);
			//p = run.exec(python_main_file);;
			
			//String line;
			//while ((line = input.readLine())!= null) {
			//	System.out.print(line);
			//}
			//Thread.currentThread().sleep(1000);
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
		return move_distance;
	}
	
	public static void main(String[] args){
		
		
		SliderVerCode find = new SliderVerCode(null, null, null);
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
		
		interpreter.execfile("./PythonFile/MoveSlider.py");
		
	}
}

***/




