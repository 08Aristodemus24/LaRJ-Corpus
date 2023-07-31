import openai
from openai import error
import time
import func_timeout
from bs4 import BeautifulSoup
import pandas as pd


def send_prompt(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}])
    answer = response['choices'][0]['message']['content']
    return answer



def identify_text(juris__df) -> pd.DataFrame:
    year = juris__df['year'].unique()[0]

    # populate list with all the answers of GPT 3.5
    answers = []
    file_paths = []

    # open all files extract text with a certain limit
    for itn, file_path in enumerate(juris__df.loc[:, 'file_path']):
        print(file_path)
        try:
            with open(file_path) as file:
                document = file.read()
                dom = BeautifulSoup(document, 'lxml')

                # extract text of html file
                text = dom.get_text()

                # make api call with GPT 3.5 here

                # create prompt with this random jurisprudence file
                prompt = f"""{text[:17000]}

                Read and identify carefully whether this piece of case law is labor related or not labor related. Answer only in binary terms "labor related" or "not labor related"""
                # print(prompt)

                # feed prompt to chat gpt to helper function func timeout to catch
                # unresponsive rqeuests or requests that take to long. Will raise error if
                # it takes too long
                answer = func_timeout.func_timeout(40, send_prompt, args=(prompt,))

                # append response if successful
                # print(f'response: {answer}')
                answers.append(answer)
                file_paths.append(file_path)
                
                # close file
                file.close()
        except error.Timeout:
            print('server has timed out retrying prompt')

            # record what answers have been generated before error
            # record what file path did the error occured
            # pd.DataFrame({'file_path': file_paths,'answer': answers})
            answers.append('TIMEOUT_ERROR')
            file_paths.append(file_path)

        except error.RateLimitError:
            print('Rate limit reached for default-gpt-3.5-turbo in organization org-lQNgFbb5falHwdZD3HS05eya on requests per min. Limit: 20 / min. Please try again in 3s')
            
            # record what answers have been generated before error
            # record what file path did the error occured
            # pd.DataFrame({'file_path': file_paths,'answer': answers})
            answers.append('RATE_LIMIT_ERROR')
            file_paths.append(file_path)

            # initiate 5 second delay
            print('5 second delay occuring')
            time.sleep(5.0)

        except error.ServiceUnavailableError as e:
            print(e._message)

            # pd.DataFrame({'file_path': file_paths,'answer': answers})
            answers.append('SERVICE_UNAVAILABLE_ERROR')
            file_paths.append(file_path)

        except error.InvalidRequestError as e:
            print(e._message)

            # pd.DataFrame({'file_path': file_paths,'answer': answers})
            answers.append('INVALID_REQUEST_ERROR')
            file_paths.append(file_path)

        except func_timeout.FunctionTimedOut:
            print('Request took too long will move to next file')

            # pd.DataFrame({'file_path': file_paths,'answer': answers})
            answers.append('TIME_LIMIT_REACHED')
            file_paths.append(file_path)

        except error.APIConnectionError:
            print('Error communicating with OpenAI')

            # 
            answers.append('API_CONNECTION_ERROR')
            file_paths.append(file_path)

        finally:
            print('Moving on. Waiting for 5 seconds to avoid traffic')
            answers_partial = pd.DataFrame({'file_path': file_paths,'answer': answers})
            answers_partial.to_csv(f'./answers_{year}__partial.csv')
            time.sleep(5.0)


    return pd.DataFrame({'file_path': file_paths,'answer': answers})
            


def read_content(juris__df):
    # open all files extract text with a certain limit
    for itn, file_path in enumerate(juris__df.loc[:, 'file_path']):
        print(file_path)
        with open(file_path) as file:
            # read file
            document = file.read()

            # pass document to beautiful soup 
            dom = BeautifulSoup(document, 'lxml')

            # now able to access html elements
            # so extract text of html file
            text = dom.get_text()

            # log every 100th iteration
            if itn % 100 == 0:
                print(text)

            # close file
            file.close()


