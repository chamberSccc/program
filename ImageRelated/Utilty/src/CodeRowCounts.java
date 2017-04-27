import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class CodeRowCounts {
	
	public static void main(String[] args){
		CodeRowCounts crc = new CodeRowCounts();
		crc.getFileName();
	}
	
	private void getFileName(){
		int rowCount = 0;
		String path="d:/chenbo/aaaaaa/b";
		File file=new File(path);
		File[] fileList = file.listFiles();
		for(int i=0;i<fileList.length;i++){
			rowCount += this.readFileByLines(fileList[i].toString());
		}
		System.out.println("代码有"+rowCount+"行");
	}
	//按行读取文件
	private int readFileByLines(String fileName){
		int line = 0;
		File file = new File(fileName);
		BufferedReader reader = null;
		try {
			reader = new BufferedReader(new FileReader(file));
			String tempText = null;
			while((tempText=reader.readLine())!= null){
				if(tempText.trim().length()!=0){
					line++;
				}
				
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return line;
	}
	

	
}
