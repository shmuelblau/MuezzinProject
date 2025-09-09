from faster_whisper import WhisperModel
import io

class Transcriber:
      
      model = WhisperModel("base")

      @staticmethod
      def get_text( file:bytes)->str:
            segments, info = Transcriber.model.transcribe(io.BytesIO(file))

            text = ".".join([s.text for s in segments])
            return text

      


      
      
      


