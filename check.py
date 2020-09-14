import pythonwhois

from joblib import Parallel, delayed, cpu_count

n_jobs = 100

def f(domain):
    details = pythonwhois.get_whois(domain)
    if 'No match for' in str(details):   # simple but it works!
        print(domain)
        return domain
    else:
        return None

domains= ['hello.com', 'helloworld.com', 'goodDomain.com']
result = Parallel(n_jobs=n_jobs, verbose=10)(delayed(f)(domain) for domain in domains)

available_domains=[domains[idx] for idx,r in enumerate(result) if r!=None]
print(available_domains)
